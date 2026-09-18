"""
Задача 1

Дан список чисел. Поменять местами первый и последний четные элементы.

Примеры:
Дано: [5, **8**, 7, 3, 10, 11, **4**, 9] Результат: [5, 4, 7, 3, 10, 11, 8, 9]
Дано: [**12**, 5, 7, **6**, 9] Результат: [6, 5, 7, 12, 9]
"""


source = [5, 8, 7, 3, 10, 11, 4, 9]
# source = [12, 5, 7, 6, 9]
# source = []
# source = [4]
# source = [1]

print(source)

lhs = None
rhs = None

for i in range(len(source)):
    if source[i] % 2 == 0:
        lhs = i
        break

for i in range(-1, -len(source) - 1, -1):
    if source[i] % 2 == 0:
        rhs = i
        break

if lhs and rhs:
    source[lhs], source[rhs] = source[rhs], source[lhs]

print(source)
