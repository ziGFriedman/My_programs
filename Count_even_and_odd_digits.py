'''Посчитать четные и нечетные цифры числа'''
# Определить, сколько в числе четных цифр, а сколько нечетных. Число вводится с клавиатуры.
# Если число делится без остатка на 2, его последняя цифра четная. Увеличиваем на 1 счетчик
# четных цифр even. Иначе последняя цифра числа нечетная, увеличиваем счетчик нечетных цифр odd.
def even_odd(x: int):
    even = 0
    odd = 0
    while x > 0:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
        x //= 10
    print('Even: {}, odd: {}'.format(even, odd))

even_odd(134)
