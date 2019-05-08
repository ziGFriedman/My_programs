'''В строке заменить пробелы символом *'''
# В строке заменить пробелы звездочкой. Если встречается подряд несколько
# пробелов, то их следует заменить одним знаком "*", пробелы в начале и конце
# строки удалить.

# Решение данной задачи классическим способом
s = input()

i = 0
while s[i] == ' ': i += 1
s = s[i:]

i = len(s)
while s[i - 1] == ' ': i -= 1
s = s[:i]

s1 = s[0]
i = 1
while i < len(s):
	if s[i] != ' ':
		s1 += s[i]
	elif s[i - 1] != ' ':
		s1 += '*'
	i += 1
print(s1 + '!')

# С помощью метода split() строка разделяется на слова по пробелам. При этом
# неважно сколько их. Далее остается только снова собрать слова в строку. Проще
# это сделать строковым методом join():
print("*".join(input().split()))

# s = input()
# l = s.split()
# s1 = '*'.join(l)
# print(s1)
