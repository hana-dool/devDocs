def leap_year(year):
    """ year 가 윤년이면 True 아니면,  False리턴 
    
    Example
    -------
    >>> leap_year(1)
    False
    >>> leap_year(4)
    True
    >>> leap_year(1200)
    True
    >>> leap_year(700)
    False
    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
