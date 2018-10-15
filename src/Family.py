import sys
import datetime 

class Family():
    row_headers = [
                    "ID", "Married", "Divorced", "Husband ID", "Husband Name",
                    "Wife ID", "Wife Name", "Children"
    ]
    error_header = "ERROR: FAMILY:"
    anomaly_header = "ANOMALY: FAMILY"

    def __init__(self, id, husband, wife, married_date, div_date=None, children=None):
        id.replace('@', '')
        self.id = id
        self.husband = husband
        self.wife = wife
        self.married_date = married_date
        self.div_date = div_date
        if children is not None:
            self.children = children
        else:
            self.children = []
        self.errors = []
        self.anomalies = []
        
        self.validate()
    
    def validate(self):
        self._check_dates()
       
    def _add_error(self, story, error):
        self.errors.append("%s %s: %s: %s" % 
                (Family.error_header, story, self.id, error))

    def _add_anomaly(self, story, anomaly):
        self.anomalies.append("%s %s: %s: %s" %
                (Family.anomaly_header, story, self.id, anomaly))
                
    def _check_names(self):
        if self.husband is not None and self.children is not None:
            temp = self.husband.name
            temp = temp.split("/")
            temp = temp[1]
            for child in self.children:
                if child.gender == "M":
                    lastname = child.name
                    lastname = lastname.split("/")
                    lastname = lastname[1]
                    if temp != lastname:
                        self._add_anomaly("US16", "Male lastnames don't match!")            
    def _check_siblings(self):
        if len(self.children) > 14:
            self._add_anomaly("US15", "Siblings not fewer then 15")
    def _check_dates(self):
        now = datetime.datetime.now()

        if self.husband is not None and self.wife is not None:

            # Validate marriage date
            if self.married_date is not None:
                # Married before current date
                if self.married_date > now:
                    self._add_error("US01", "Marriage date %s occurs in the future" % self.married_date.strftime("%Y-%m-%d"))
                # Birth before marriage - husband
                if self.husband.bday > self.married_date:
                    self._add_error("US02", "Husband's birth date %s after marriage date %s" % (self.husband.bday.strftime("%Y-%m-%d"), self.married_date.strftime("%Y-%m-%d")))
                # Birth before marriage - wife
                if self.wife.bday > self.married_date:
                    self._add_error("US02", "Wife's birth date %s after marriage date %s" % (self.wife.bday.strftime("%Y-%m-%d"), self.married_date.strftime("%Y-%m-%d")))
                    
                # Marriage before death - husband 
                if not self.husband.alive and self.husband.death < self.married_date:
                    self._add_error("US05", "Married %s after husband's (%s) death on %s" % (self.married_date.strftime('%Y-%m-%d'), self.husband.id, self.husband.death.strftime('%Y-%m-%d')))
                # Marriage before death - wife
                if not self.wife.alive and self.wife.death < self.married_date:
                    self._add_error("US05", "Married %s after wife's (%s) death on %s" % (self.married_date.strftime('%Y-%m-%d'), self.wife.id, self.wife.death.strftime('%Y-%m-%d')))
                
                # Marriage under 14 years old
                if self.married_date.year - self.husband.bday.year < 14:
                    self._add_error("US10", "Under 14 at time of marriage - Birth %s: Marriage %s" % (self.husband.bday.strftime("%Y-%m-%d"), self.married_date.strftime("%Y-%m-%d")))
                if self.married_date.year - self.wife.bday.year < 14:
                    self._add_error("US10", "Under 14 at time of marriage - Birth %s: Marriage %s" % (self.wife.bday.strftime("%Y-%m-%d"), self.married_date.strftime("%Y-%m-%d")))
                    
                for child in self.children:
                # Validate child birth is after parents marriage
                    if child.bday < self.married_date:
                        self._add_anomaly("US08", "Child %s born %s before marriage on %s" % (child.id, child.bday.strftime("%Y-%m-%d"), self.married_date.strftime("%Y-%m-%d")))
                # Validate child birth is before parents death
                    if not self.wife.alive and not self.husband.alive:    
                        if child.bday > self.wife.death:
                            self._add_error("US09", "Child %s born on %s after father's death on %s" % (child.id, child.bday.strftime('%Y-&m-%d'), self.husband.death.strftime('%Y-&m-%d')))
                        if child.bday > self.husband.death:
                            self._add_error("US09", "Child %s born on %s after mother's death on %s" % (child.id, child.bday.strftime('%Y-&m-%d'), self.wife.death.strftime('%Y-&m-%d')))
                        
                        
            
            # Validate divorce date
            if self.div_date is not None:
                # Divorce before current date
                if self.div_date > now:
                    self._add_error("US01", "Divorce date %s occurs in the future" % self.div_date.strftime("%Y-%m-%d"))
                # Divorce before death - husband
                if not self.husband.alive and self.husband.death < self.div_date:
                    self._add_error("US06", "Divorced %s after husband's (%s) death on %s" % (self.div_date.strftime('%Y-%m-%d'), self.husband.id, self.husband.death.strftime('%Y-%m-%d')))
                # Divore before death - wife
                if not self.wife.alive and self.wife.death < self.div_date:
                    self._add_error("US06", "Divorced %s after wife's (%s) death on %s" % (self.div_date.strftime('%Y-%m-%d'), self.wife.id, self.wife.death.strftime('%Y-%m-%d')))
                # Divorce before marriage
                if self.married_date is not None and self.div_date < self.married_date:
                    self._add_error("US04", "Divorced %s before married %s" % (self.div_date.strftime('%Y-%m-%d'), self.married_date.strftime('%Y-%m-%d')))
            
                    
    @staticmethod
    def instance_from_dict(fam_dict):
        id = fam_dict['FAM']
        husband = fam_dict["HUSB"]
        wife = fam_dict["WIFE"]

        husband.add_spouse(wife)
        wife.add_spouse(husband)

        married_date = datetime.datetime.strptime(fam_dict["MARR"], '%d %b %Y')
        children = [] 
        div_date = None

        if "CHIL" in fam_dict:
            children = fam_dict["CHIL"]
            husband.children = children
            wife.children = children

        if "DIV" in fam_dict:
            div_date = datetime.datetime.strptime(fam_dict["DIV"], '%d %b %Y')

        return Family(id, husband, wife, married_date, div_date=div_date, children=children)

    def print_anomalies(self):
        for i in self.anomalies:
            print(i, file=sys.stderr)

    def print_errors(self):
        for i in self.errors:
            print(i, file=sys.stderr)

    def to_row(self):
        ret = []
        ret.append(self.id)
        ret.append('NA' if self.married_date is None else self.married_date.strftime('%Y-%m-%d'))

        ret.append('NA' if self.div_date is None else self.div_date.strftime('%Y-%m-%d'))


        ret.append(self.husband.id)
        ret.append(self.husband.name)
        ret.append(self.wife.id)
        ret.append(self.wife.name)

        if len(self.children) > 0:
            ret.append('{%s}' % ','.join(list(map(lambda x: x.id, self.children))))
        else:
            ret.append('NA')

        return ret
    
    def __str__(self):
        return str(dict(zip(Family.row_headers, self.to_row())))

