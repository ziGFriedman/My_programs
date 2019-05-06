'''Простейший калькулятор'''
# Написать программу, которая выполняет над двумя вещественными числами одну из четырех
# арифметических операций (сложение, вычитание, умножение или деление). Программа должна
# завершаться только по желанию пользователя.
# Чтобы программа самопроизвольно не завершалась, в ней надо запустить бесконечный цикл.
# Выход из него будем осуществлять с помощью оператора break, если пользователь вводит
# определенный символ вместо знака арифметической операции.
# Если пользователь ввел знак, который не является ни знаком арифметической операции, ни
# символом-"прерывателем" работы программы, то вывести сообщение о некорректном вводе.
# Если был введен один из четырех знаков операции, запросить ввод двух чисел.
# В зависимости от знака операции выполнить соответствующее арифметическое действие.
# Если было выбрано деление, необходимо проверить не является ли нулем второе число. Если
# это так, то сообщить о невозможности деления.
print("Ноль в качестве знака операции завершит работу программы")
while True:
    s = input('Знак (+,-,*,/): ')
    if s == '0': break
    if s in ('+','-','*','/'):
        x = float(input('x = '))
        y = float(input('y = '))
        if s == '+':
            print('{:.2f}'.format(x + y))
        elif s == '-':
            print('{:.2f}'.format(x - y))
        elif s == '*':
            print('{:.2f}'.format(x * y))
        elif s == '/':
            if y != 0:
                print('{:.2f}'.format(x / y))
            else:
                print('Деление на ноль!')
    else:
        print('Неверный знак операции!')