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
    if birth == '' or birth == 'N/A' or birth == 'Unknown':
        return False
    if death == '' or death == 'N/A' or death == 'Unknown':
        return False
    date_int = { "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12 }
    birth = birth.split('-')
    death = death.split('-')

    if eval(death[2]) - eval(birth[2]) > 150:
        return True
    elif eval(death[2]) - eval(birth[2]) == 150:
        if date_int[death[1]] > date_int[birth[1]]:
            return True
        elif date_int[death[1]] == date_int[birth[1]]:
            if death[0] > birth[0]:
                return True
    return False

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