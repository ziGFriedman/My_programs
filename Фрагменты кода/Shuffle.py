# Этот код можно использовать для рандомизации порядка элементов в списке. Обратите внимание, что
# shuffle работает на месте и возвращает None:
from random import shuffle

foo = [1, 2, 3, 4]
shuffle(foo)
print(foo) # [1, 4, 3, 2] , foo = [1, 2, 3, 4]
