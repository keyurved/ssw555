import datetime

class Individual():
    row_headers = [
                    "ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Children",
                    "Spouse"
    ]

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
        self.validate()

    def validate(self):
        self._check_dates()
  
    
    def _check_dates(self):
        now = datetime.datetime.now()
        
        # Birth and death dates before current date
        if self.alive:
            if self.bday > now:
                raise ValueError("Birth date %s cannot be after the current date %s" % (self.alive.strftime('%Y-%m-%d'), now.strftime('%Y-%m-%d %H:%M')))
        if self.death is not None:
            if self.death > now:
                raise ValueError("Death date %s cannot be after the current date %s" % (self.death.strftime('%Y-%m-%d'), now.strftime('%Y-%m-%d %H:%M')))
                    
                                                      
                        
    @staticmethod
    def instance_from_dict(info_dict):
        id = info_dict['INDI']
        name = info_dict['NAME']
        gender = info_dict['SEX']
        bday = datetime.datetime.strptime(info_dict['BIRT'], '%d %b %Y').date()
        today = datetime.datetime.today()
        age = today.year - bday.year - ((today.month, today.day) < (bday.month, bday.day))
        families = info_dict['FAM']
        alive = True
        death = None

        if 'DEAT' in info_dict.keys():
            alive = False
            death = datetime.datetime.strptime(info_dict['DEAT'], '%d %b %Y').date()

        
        return Individual(id, name, gender, bday, age, families, alive, death=death)

    def add_child(self, child):
        self.children.append(child)

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
