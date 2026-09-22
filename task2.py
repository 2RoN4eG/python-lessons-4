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
source = [12, 3, 4, 14, 5, 6, 7, 4, 14, 3, 5]

sorted = source.copy()
sorted.sort()

minimum = sorted[0]
maximum = sorted[-1]

print("maximum is", maximum)
print("minimum is", minimum)

lhs = None
rhs = None

minimum_found = False
maximum_found = False

for index in range(len(source)):
    value = source[index]
    if value == maximum:
        lhs = index
        maximum_found = True
        break
    elif value == minimum:
        lhs = index
        minimum_found = True
        break

for index in range(len(source)):
    last = len(source) - index - 1
    value = source[last]
    if value == maximum and not maximum_found:
        rhs = last
        break
    elif value == minimum and not minimum_found:
        rhs = last
        break

print("lhs is", lhs)
print("rhs is", rhs)

# sum_ = 0
# for index in range(lhs + 1, rhs):
#     value = source[i]
#     sum_ += value

slice_sum = sum(source[lhs + 1: rhs])

# print('sum is', sum_)
print('sum is', slice_sum)
