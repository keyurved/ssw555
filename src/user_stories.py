import datetime


def US23(fam):
    members = len(fam)
    dates = [None] * (members+1)
    names = [None] * (members+1)
    counter = 0
    for member in fam:
        name = member[0]
        date = member[1]
        if name in names:
            index = names.index(name)
            date_comp = dates[index]
            if date == date_comp:
                return False
            else:
                dates[counter] = date
                names[counter] = name
        else:
            dates[counter] = date
            names[counter] = name
        counter+=1
    return True
            


def US24(date):
    #Takes in a string and returns wether it is a valid date in the format DD-MM-YYYY
    try:
        make_date_possible = datetime.datetime.strptime(date, '%d %b %Y')
    except:
        return False #If try block fails, date is invalid, return False
    return True #If try block succeeds go to here

def US31(date):
    married_date_in = date
    curr_year = datetime.datetime.now().year
    married_date_in = married_date_in.replace(year=curr_year)
    check = married_date_in - datetime.datetime.now()
    if check.days<30 and check.days>0:
        return True
    return False
def US32(date):
    married_date_in = date
    curr_year = datetime.datetime.now().year
    married_date_in = married_date_in.replace(year=curr_year)
    check = married_date_in - datetime.datetime.now()
    if check.days<30 and check.days>0:
        return True
    return False