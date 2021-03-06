'''Проверка гипотезы Сиракуз'''
# Гипотеза Сиракуз гласит, что любое натуральное число сводится к единице при следующих
# действиях над ним: а) если число четное, то разделить его пополам, б) если число нечетное,
# то умножить его на 3, прибавить 1 и результат разделить на 2. Над вновь полученным
# числом вновь повторить действия a) или б) в зависимости от четности числа. Рано или
# поздно число станет равным 1.
def syracuse(n: int):
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2
        print(n, end=' ')

syracuse(56)
