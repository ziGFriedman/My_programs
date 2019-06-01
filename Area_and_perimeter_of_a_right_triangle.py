'''Найти площадь и периметр прямоугольного треугольника'''
# Найти площадь и периметр прямоугольного треугольника по двум заданным катетам.
# Площадь прямоугольного треугольника равна половине площади прямоугольника, стороны которого равны
# длинам катетов.
# Периметр находится путем сложения длин всех сторон треугольника. Поскольку известны только катеты,
# гипотенуза вычисляется по теореме Пифагора:
# c2 = a2 + b2
# Чтобы извлечь квадратный корень в Python, можно воспользоваться функцией sqrt() из модуля math.
import math

AB = float(input("Длина первого катета: "))
AC = float(input("Длина второго катета: "))

BC = math.sqrt(AB ** 2 + AC ** 2)
S = (AB * AC) / 2
P = AB + AC + BC

print("Площадь треугольника: {0:.2f}".format(S))
print("Периметр треугольника: {0:.2f}".format(P))
