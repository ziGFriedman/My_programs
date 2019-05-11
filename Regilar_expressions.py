'''Пример использования регулярных выражений'''
import re

if __name__ == '__main__':
    name_pattern = r'My name is .*\.'    # r - выключает специальные символы
    is_name = re.match(name_pattern, 'My name is Nikolay.')    # match - проверяет на соответствие
    print('is name:', bool(is_name))

    is_name = re.match(name_pattern, 'I am just a string.')
    print('is name:', bool(is_name))

    name_pattern_group = r'My name is (.*)\.'    # (.*) - группа
    name = re.findall(name_pattern_group, 'My name is Nikolay.')    # findall - забрать что-то из выражения
    print(name)
