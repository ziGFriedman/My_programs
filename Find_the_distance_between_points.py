'''Найти расстояние между точками в n-мерном пространстве'''
# Найти расстояние между точками с заданными координатами в n-мерном пространстве.
# Расстояние находится по формуле d = sqrt((a1 - b1)2 + (a2 - b2)2 + ... + (an - bn)2),
# где sqrt - квадратный корень, а1...an - координаты первой точки, b1..bn -
# соответствующие координаты второй точки.
# Чтобы не вводить каждую координату отдельно, можно запросить сразу все для каждой
# точки. Поскольку данные будут иметь строковый тип, то преобразовать их к списку
# можно с помощью функции split(). В качестве аргумента функции передается
# строка-разделитель, по которому отделяются элементы; если аргумент отсутствует,
# то строка разделяется по пробелу. Несмотря на такое разделение, каждый элемент
# списка по-прежнему является строкой, а не числом.
# Функция zip() возвращает кортежи соответствующих элементов последовательностей.
# Т.е. если ей передать два списка, то на первой итерации будет возвращен кортеж
# из первых элементов обоих списков, на второй - из вторых и т. д.
import math

n = input('Количество измерений пространства: ')
print('Через пробел')
a = input('введите ' + n + ' координаты 1-ой точки: ')
b = input('введите ' + n + ' координаты 2-ой точки: ')
n = int(n)
a = a.split()
b = b.split()
if len(a) != n or len(b) != n:
	print('Неверный ввод!')
	exit()

sum_sqr = 0
for i, j in zip(a, b):
	sum_sqr += (int(i) - int(j)) ** 2
distance = math.sqrt(sum_sqr)
print('Расстояние между точками: {:.2f}'.format(distance))