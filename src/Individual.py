import sys
import datetime
from user_stories import US23, US24

class Individual():
    row_headers = [
            "ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death",
            "Children", "Spouse"
    ]

    error_header = "ERROR: INDIVIDUAL:"

    def __init__(self, id, name, gender, bday, age, familes, alive, death=None, children=None, spouses=None):
        if '@' in id:
            id.replace('@', '')
        self.id = id
        self.name = name
        self.gender = gender
        self.bday = bday
        self.age = age
        self.alive = alive
        self.families = familes
        self.death = death
        if children is None:
            self.children = []
        else:
            self.children = children

        if spouses is None:
            self.spouses = []
        else:
            self.spouses = spouses
        self.errors = []
        self.validate()

    def validate(self):
        self._check_dates()


    def _add_error(self, story, error):
        self.errors.append("%s %s: %s: %s" % 
                (Individual.error_header, story, self.id, error))

    def _check_dates(self):
        now = datetime.datetime.now()

        # Birth and death dates before current date
        if self.bday is not None and self.bday > now:
            self._add_error("US01", "Birthday %s occurs in the future" % (self.bday.strftime('%Y-%m-%d')))
        elif self.death is not None:
            if self.death > now:
                self._add_error("US01", "Death %s occurs in the future" % (self.death.strftime('%Y-%m-%d')))
            # Death before birth
            if self.death < self.bday:
                self._add_error("US03", "Died %s before born %s" % (self.death.strftime('%Y-%m-%d'), self.bday.strftime('%Y-%m-%d')))
            # Died over 150 years old
            if abs(self.death.year - self.bday.year) > 150:
                self._add_error("US07", "More than 150 years old at death - Birth %s: Death %s" % (self.bday.strftime("%Y-%m-%d"), self.death.strftime("%Y-%m-%d")))
        # Over 150 and still alive        
        elif abs(now.year - self.bday.year) > 150:
            self._add_error("US07", "More than 150 years old - Birth %s" % (self.bday.strftime("%Y-%m-%d")))

    def print_errors(self):
        for i in self.errors:
            print(i, file=sys.stderr)

    @staticmethod
    def instance_from_dict(info_dict):
        id = info_dict['INDI']
        name = info_dict['NAME']
        gender = info_dict['SEX']

        if 'BIRT' in info_dict.keys():
            try:
                abbrev_to_num = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}
                check_valid = info_dict['BIRT']
                check_valid = check_valid.split(" ")
                check_valid[1] = str(abbrev_to_num[check_valid[1]])
                check_valid = "-".join(check_valid)
                if(US24(check_valid)):
                    pass
                else:
                    print('Invalid Date: ', info_dict['BIRT'])
                bday = datetime.datetime.strptime(info_dict['BIRT'], '%d %b %Y')
            except:
                print("ERROR: INVALID DATE")
                bday = bday = datetime.datetime.strptime('01 Jan 1900', '%d %b %Y')
        else:
            bday = datetime.datetime.strptime('01 Jan 1900', '%d %b %Y')

        today = datetime.datetime.today()
        age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
        families = info_dict['FAM']
        alive = True
        death = None

        if 'DEAT' in info_dict.keys():
            alive = False
            death = datetime.datetime.strptime(info_dict['DEAT'], '%d %b %Y')
        return Individual(id, name, gender, bday, age, families, alive, death=death)

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, children):
        for child in children:
            self.add_child(child)
    def add_spouse(self, sp):
        self.spouses.append(sp)

    def set_spouse(self, spouse):
        if spouse not in self.spouses:
            self.spouses.append(spouse)

    def to_row(self):
        ret = []

        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.gender)
        ret.append(self.bday.strftime('%Y-%m-%d'))
        ret.append(self.age)

        ret.append('True' if self.alive else 'False')

        ret.append('NA' if self.alive else self.death.strftime('%Y-%m-%d'))

        if len(self.children) > 0:
            ret.append("{%s}" % ','.join(list(map(lambda x: x.id, self.children))))
        else:
            ret.append('NA')

        if len(self.spouses) > 0:
            ret.append("{%s}" % ','.join(list(map(lambda x: x.id, self.spouses))))
        else:
            ret.append('NA')
        return ret

    def __str__(self):
        return str(dict(zip(Individual.row_headers, self.to_row())))
