'''Найти произведение первого, третьего и шестого положительных элементов массива'''
# В списке, состоящем из положительных и отрицательных целых чисел, найти первый,
# третий и шестой положительные элементы и вычислить их произведение.
# Основная часть алгоритма решения задачи:
# Ввести в программу счетчик положительных элементов (j). Присвоить ему значение 1
# (т.е. он указывает на первый положительный элемент).
# Перебирать элементы массива-списка по-очереди. Если очередной элемент положительный
# и счетчик положительных элементов равен 1 или 3 или 6, то сохранить в соответствующей
# переменной индекс данного элемента. Кроме того, если шестой положительный элемент
# найден, то нет смысла продолжать цикл дальше и можно его завершить (оператор break).
# Если в массиве был найден шестой положительный элемент (первый и третий тогда точно
# найдены), то вычислить произведение.
# В программе ниже для заполнения списка используется так называемый генератор. В
# данном случае выражение round(random.random() * 100) - 50 используется в цикле,
# который выполняется 20 раз. И на каждой итерации цикла получившееся число помещается
# в список a.
import random

a = [round(random.random() * 100) - 50 for i in range(20)]
print(a)

i = j = 0
i1 = i3 = i6 = -1

while i < 20:
	if a[i] > 0:
		if j == 1:
			i1 = i
		elif j == 3:
			i3 = i
		elif j == 6:
			i6 = i
			break
		j += 1
	i += 1
if i6 > 0:
	mult = a[i1] * a[i3] * a[i6]
	print('Индексы элементов:', i1, i3, i6)
	print('{} * {} * {} = {}'.format(a[i1], a[i3], a[i6], mult))