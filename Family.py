import datetime 

class Family():
    row_headers = [
                    "ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID",
                    "Wife Name", "Children"
    ]

    def __init__(self, id, husband, wife, married_date, div_date=None, children=None):
        id.replace('@', '')
        self.id = id
        self.husband = husband
        self.wife = wife
        self.married_date = married_date
        self.div_date = div_date
        if children is None:
            self.children = children
        else:
            self.children = []
    
    @staticmethod
    def instance_from_dict(fam_dict):
        id = fam_dict['FAM']
        husband = fam_dict["HUSB"]
        wife = fam_dict["WIFE"]

        husband.add_spouse(wife)
        wife.add_spouse(husband)

        married_date = datetime.datetime.strptime(fam_dict["MARR"], '%d %b %Y').date()
        children = [] 
        div_date = None

        if "CHIL" in fam_dict:
            children = fam_dict["CHIL"]
            husband.children = children
            wife.children = children

        if "DIV" in fam_dict:
            div_date = datetime.datetime.strptime(fam_dict["DIV"], '%d %b %Y').date()

        return Family(id, husband, wife, married_date, div_date=div_date, children=children)

    def to_row(self):
        ret = []
        ret.append(self.id)
        ret.append(self.married_date.strftime('%Y-%m-%d'))

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
