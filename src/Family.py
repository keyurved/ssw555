import sys
import datetime 
from collections import Counter
from dateutil import relativedelta as rd

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
        self._check_names()
        self._check_parents()
        self._check_marriages()
        self._check_marriages2()


        if len(self.children) > 0:
            self._check_siblings()
            self._validate_children()
       
    def _add_error(self, story, error):
        self.errors.append("%s %s: %s: %s" % 
                (Family.error_header, story, self.id, error))

    def _add_anomaly(self, story, anomaly):
        self.anomalies.append("%s %s: %s: %s" %
                (Family.anomaly_header, story, self.id, anomaly))
                        
    def _check_marriages(self):
        #US18 Siblings should not marry 
        if self.children is not None:
            for child in self.children:
                if child.spouses is not None:
                    for spouse in child.spouses:
                        if child.gender == 'M' and child.spouses is not None:                    
                            self._add_anomaly("US18", "Spouse cannot be your sister")
                        if child.gender == 'F' and child.spouses is not None:
                            self._add_anomaly("US18", "Spouse cannot be your brother")
    


    # def _helper_marriages(self,temp,childrenList):
    #     for child in temp:
    #         childrenList.append(child)
    #         if child.children != [] or child.children !='NA':
    #             temp.append(child.children)
    #             temp.remove(child)
    #         else:
    #             temp = temp
    #     return temp, childrenList
    # 
    # def _check_marriages2(self):
    #     #US17 No marriages to descendants
    #     print(self)
    #     childrenList = []
    #     temp = self.children
    #     while temp != []:            
    #         self._helper_marriages(temp,childrenList)
    #         print("hello")

    
    def _check_marriages2(self):
        #US17 No marriages to descendants
        childrenList = []
        temp = self.children
        # if self.children is not None:
        #     while temp != []:           
        #         for child in self.children:
        #             print(child)
        #             childrenList.append(child)
        #             if child.children is not None:
        #                 temp.append(child.children)
        #                 temp.remove(child)
        #             else:
        #                 temp = temp  
        if self.children is not None:
            while temp != []:
                for child in temp:
                    childrenList.append(child)
                    if child.children != []:
                        #for thing in child.children:
                        temp.append(child.children)
                        temp.remove(child)
                    else:
                        temp = []               
         
    def _check_parents(self):
        if self.husband is not None and self.husband.gender != 'M':
            self._add_anomaly("US21", "Husband's gender is not M")
        if self.wife is not None and self.wife.gender != 'F':
            self._add_anomaly("US21", "Wife's gender is not F")
    def _validate_children(self):
        child_sorted = sorted(self.children, key=lambda x: x.bday)
        count_bdays = Counter()

        for i in range(len(child_sorted)):
            # Children born too close together
            first = child_sorted[i]
            for j in range(i + 1, len(child_sorted)):
                second = child_sorted[j]
                diff = rd.relativedelta(second.bday, first.bday)

                if abs(diff.months) < 8 and abs(diff.days) > 2 and abs(diff.months) > 0:
                    self._add_error("US13", "Children's bdays are less than 8 months and are not twins %s: %s %s: %s" \
                                    % (first.id, first.bday.strftime("%Y-%m-%d"), second.id, second.bday.strftime("%Y-%m-%d")))

            # More than 5 children on the same day
            if len(count_bdays.keys()) == 0:
                count_bdays[first.bday] += 1
            else:
                added = False
                for key in count_bdays.keys():
                    diff2 = rd.relativedelta(first.bday, key)

                    if abs(diff2.days) <= 2 and diff2.months == 0:
                        added = True
                        count_bdays[key] += 1

                        if count_bdays[key] == 5:
                            self._add_error("US14", "More than 5 children born on: %s" % key.strftime("%Y-%m-%d"))
                        break

                if not added:
                    count_bdays[first.bday] += 1

                
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


    # def _add_anomaly(self, story, anomaly):
    #     self.anomalies.append("%s %s: %s: %s" %
    #             (Family.anomaly_header, story, self.id, anomaly))
        
    #Method to add error for bigomy within the family      
    def bigError(self,person):
        self._add_error("US12", "Person %s cannot have another marriage without getting the first one divorced." %(person.id))
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
                    if not self.wife.alive and child.bday > self.wife.death:
                        if child.bday > self.wife.death:
                            self._add_error("US09", "Child %s born on %s after mother's death on %s" % (child.id, child.bday.strftime('%Y-%m-%d'), self.wife.death.strftime('%Y-%m-%d')))
                    if not self.husband.alive and child.bday > self.husband.death:
                            self._add_error("US09", "Child %s born on %s after father's death on %s" % (child.id, child.bday.strftime('%Y-%m-%d'), self.husband.death.strftime('%Y-%m-%d')))
            
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

        # Validate age of children compared too the age of children
        if self.children is not None:
            for child in self.children:
                #Check if Father is not older than 80 years
                if self.husband is not None and (self.husband.age - child.age) > 80:
                    self._add_error("US12", "Father is %s years older than his child." % (self.husband.age - child.age))
                #Check if Mother is not older than 60 years
                if self.wife is not None and (self.wife.age - child.age) > 60:
                    self._add_error("US11", "Mother is %s years older than her child." % (self.wife.age - child.age))
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
            husband.add_children(children)
            wife.add_children(children)

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

