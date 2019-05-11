'''Удаление элементов списка по условию'''
# Из списка чисел удалить элементы, значения которых больше 35 и меньше 65. При
# этом удаляемые числа сохранить в другом списке.
# В Python с помощью инструкции del можно удалить элемент списка, указав сам
# список и индекс удаляемого элемента.
# Алгоритм решения задачи выглядит простым. Достаточно перебрать элементы списка
# и удалить те, которые удовлетворяют условию. Однако при удалении элемента на его
# место становится следующий, но поскольку мы переходим к следующему элементу, то
# пропускаем проверку того, что стал на место удаленного. Цикл for использовать
# нельзя, т. к. меняется количество элементов списка.
# Можно использовать цикл while, измеряя на каждой его итерации длину списка,
# индекс же увеличивать только в том случае, если удаления элемента не произошло.
import random

a = []
for i in range(20):
	n = round(random.random() * 100) # от 0 до 100 включительно
	a.append(n)
print('A =', a)

b = []
i = 0
while i < len(a):
	if 35 < a[i] < 65:
		b.append(a[i])
		del a[i]
	else:
		i += 1
print('A =', a)
print('B =', b)