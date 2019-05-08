'''Проверить уникальность элементов списка'''
from random import random

N = 10
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 50)

print(arr)

for i in range(N - 1):
    for j in range(i + 1, N):
        if arr[i] == arr[j]:
            print('Есть одинаковые')
            quit()
print('Все элементы уникальны')


# setarr = set(arr)
# if len(arr) == len(setarr):
#     print("Все элементы уникальны")
# else:
#     print("Есть одинаковые")
