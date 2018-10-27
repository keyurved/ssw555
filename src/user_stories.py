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
        spl=date.split("-")
        day = int(spl[0])
        month = int(spl[1])
        year = int(spl[2])
        make_date_possible = datetime.datetime(year=year, month=month, day=day)
    except:
        return False #If try block fails, date is invalid, return False
    return True #If try block succeeds go to here