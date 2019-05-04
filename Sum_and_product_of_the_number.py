'''Находит сумму и произведение цифр числа'''
def sum_product (a):
    sum = 0
    mult = 1
    a = abs(a)
    if a == 0:
        print('Сумма:', sum, 'Произведение:', 0)
    else:
        while a > 0:
            digit = a % 10
            sum += digit
            mult *= digit
            a = a // 10
        print('Сумма:', sum, 'Произведение:', mult)

sum_product(45)
