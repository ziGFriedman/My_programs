'''Функция, возвращающая сумму чисел строки'''
def summa(a):
    a = a.split()
    b = []
    for i in a:
        b.append(int(i))
    return sum(b)

a = input()
print('Сумма:', summa(a))
