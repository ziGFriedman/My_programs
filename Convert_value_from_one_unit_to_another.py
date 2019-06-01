'''Перевести значение из одних единиц измерения в другие'''
# Пользователь вводит либо количество байт, либо килобайт, мегабайт или гигабайт. Следует перевести
# значение во все другие единицы измерения.
# В 1Кб = 1024 байт, 1Мб = 1024Кб и т. д. 1024 - это 2**10.
units = input('Выберите единицы измерения:\n \
\t1 - байты,\n \
\t2 - килобайты,\n \
\t3 - мегабайты,\n \
\t4 - гигабайты.\n№: ')

qty = float(input('Введите значение: '))

if units == '1':
	print('Килобайты: %10.3f' % (qty / 2**10))    # 10.3f - отступ 10 знаков и 3 точки после запятой
	print('Мегабайты: %10.3f' % (qty / 2**20))
	print('Гигабайты: %10.3f' % (qty / 2**30))
elif units == '2':
	print('Байты: %14d' % (qty * 2**10))    # 14d - отступ слева на 14 знаков
	print('Мегабайты: %10.3f' % (qty / 2**10))
	print('Гигабайты: %10.3f' % (qty / 2**20))
elif units == '3':
	print('Байты: %14d' % (qty * 2**20))
	print('Килобайты: %10d' % (qty * 2**10))
	print('Гигабайты: %10.3f' % (qty / 2**10))
elif units == '4':
	print('Байты: %14d' % (qty * 2**30))
	print('Килобайты: %10d' % (qty * 2**20))
	print('Мегабайты: %10d' % (qty * 2**10))
