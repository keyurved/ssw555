import datetime
def US07(birth, death):
    '''
    This function checks if a person has been alive for more than 150 years. It does so by comparing the birth and death
    dates passed to it.
    Args:
        Birth: String that contains a birth date from the gedcom file
        Death: String that contains a death date from the gedcom file
    Returns:
        True/False: True if the person has been alive for more than 150 years, otherwise False.
    '''
    if birth is None:
        return False
    if death is None:
        return False

    this_year_birthday = datetime.date(death.year, birth.month, birth.day)
    if this_year_birthday < today:
        years = death.year - birth.year
    else:
        years = death.year - birth.year - 1
    if years > 150:
        return False
    return True

def US08(birth, marriage):
    '''
    This function checks if a person was born before the marriage of their parents. It does so by comparing the birth and death
    dates passed to it.
    Args:
        Birth: datetime that contains a birth date from the gedcom file
        Marriage: datetime that contains a marriage date from the gedcom file
    Returns:
        True/False: True if the person was born before their parents marriage.
    '''
    if birth is None:
        return False
    if marriage is None:
        return False
    date_int = { "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12 }

    if birth < marriage:
        return True
    else:
        return False

#US08 Birth before marriage of parents