'''Определить количество дней в году'''
def days_per_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            year = 365
        else:
            year = 366
    else:
        year = 365
    return year

print(days_per_year(2020))
