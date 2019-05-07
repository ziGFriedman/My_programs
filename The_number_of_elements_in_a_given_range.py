'''Количество элементов, значения которых принадлежат заданному диапазону'''
# В списке найти количество элементов, значение которых не меньше заданного минимума
# и не больше заданного максимума, то есть принадлежат определенному диапазону.
# Пусть список заполняется случайными числами, границы диапазона задаются с клавиатуры.
# После того, как список заполнен и выведен на экран, запросим с клавиатуры нижнюю и
# верхнюю границы диапазона. Присвоим эти значения переменным minimum и maximum.
# Введем переменную qty, которая будет хранить количество элементов, значения которых
# попадают в диапазон. Поскольку таких элементов может и не быть, присвоим qty значение 0.
# В цикле переберем все элементы списка. Если значение очередного элемента не меньше
# minumum и не больше maximum, то к значению qty надо добавить единицу.
# Выведем значение qty на экран.
import random

arr = []
for i in range(30):
    x = int(random.random() * 100)
    arr.append(x)
    print('{}'.format(x), end = ' ')
    if (i + 1) % 5 == 0:
        print()

minimum = int(input('Min: '))
maximum = int(input('Max: '))

qty = 0
for i in arr:
    if minimum <= i <= maximum:
        qty += 1

print(qty)
