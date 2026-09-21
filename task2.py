"""
Задача 2

Дан список чисел. Найти сумму чисел между максимальным и минимальным числом в списке. 
Если максимальных/минимальных значений несколько - учитывать первое вхождение как старт и последнее как стоп.

Примеры:
Дано: [4, **1**, 7, 9, 12, 5, 3, 6, **12**] Результат: 42
Дано: [9, **15**, 7, 9, 3, 8, 3, 10, **3**] Результат: 40
"""


source = [4, 1, 7, 9, 12, 5, 3, 6, 12]
source = [9, 15, 7, 9, 3, 8, 3, 10, 3]

sorted = source.copy()
sorted.sort()

minimum = sorted[0]
maximum = sorted[-1]

lhs = None
rhs = None

minimum_found = False
maximum_found = False

for i in range(len(source)):
    value = source[i]
    if value == maximum:
        lhs = i
        maximum_found = True
        break
    elif value == minimum:
        lhs = i
        minimum_found = True
        break

for i in range(len(source)):
    value = source[len(source) - i - 1]
    if value == maximum and not maximum_found:
        rhs = len(source) - i - 1
        break
    elif value == minimum and not minimum_found:
        rhs = len(source) - i - 1
        break

sum = 0
for i in range(lhs + 1, rhs, 1):
    value = source[i]
    sum += value

print('sum is', sum)
