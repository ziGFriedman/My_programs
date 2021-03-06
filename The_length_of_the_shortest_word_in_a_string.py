'''Определить длину самого короткого слова в строке'''
# В заданной строке найти самое короткое слово.
# В Python у строкового типа данных есть метод split(), который разделяет слова
# по пробелу (или другому символу, если он передан в качестве аргумента).
# Получается список слов.
# Далее из этого списка можно извлекать отдельные слова, обращаясь к ним по индексам.
# В программе ниже сначала предполагается, что первое слово в списке и есть
# самое короткое. Остальные слова перебираются в цикле, где их длина сравнивается
# со словом в переменной shortest. Если длина текущего слова меньше, то значение
# shortest заменяется.
string = input()

words = string.split()

shortest = words[0]

for i in words[1:]:
    if len(i) < len(shortest):
        shortest = i

print(shortest)
print(len(shortest))
