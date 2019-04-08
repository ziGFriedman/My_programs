'''Символы зполнения + центровка'''
input_str = 'Jessy'

print('{0:*^10}'.format(input_str))
print('{0:>10}'.format(input_str))
print('{0:_<10}'.format(input_str))

'''Выравнивает знаки заполнения'''
input_str = 'Jessy'
length = 10

if (len(input_str) % 2):
    length += 1

print(('{0:*^'+str(length)+'}').format(input_str))
