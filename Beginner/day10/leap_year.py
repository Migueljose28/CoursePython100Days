"""
Leap year rules:
    1) add an extra day every 4 years.
    2) skip it if it's a new century.
    3) Unless the century is divisible by 400.
"""

def is_leap_year(year):
    """The fuction for calc leap years.'"""
    if year == int(str(year)[:2] + "00") :
        is_century_divisible = year%400 == 0
        return is_century_divisible
    return year%4 == 0

   
