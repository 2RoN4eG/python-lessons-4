"""
Задача 4*

Дан список температур по дням.
Нужно определить количество изменений направления:

рост → падение — одно изменение;
падение → рост — одно изменение.
Подряд идущие дни с одинаковым направлением считаются одним участком.

Пример:
[10, 12, 14, 15, 9, 5, 3, 8, 9, 10, 9] → 3
(рост → падение → рост → падение)
"""


# temperatures = [10, 12, 14, 15, 9, 5, 3, 8, 9, 10, 9]
temperatures = [10, 12, 14, 14, 15, 9, 5, 3, 8, 9, 10, 9]

clean_temps = []
for t in temperatures:
    if not clean_temps or t != clean_temps[-1]:
        clean_temps.append(t)

if len(clean_temps) < 3:
    print("Для смены направления нужно минимум 3 разные точки")
else:
    changes = 0
    current_trend = 1 if clean_temps[1] > clean_temps[0] else -1

    for i in range(2, len(clean_temps)):
        new_trend = 1 if clean_temps[i] > clean_temps[i - 1] else -1
        if new_trend != current_trend:
            changes += 1
            current_trend = new_trend

print("changes is", changes)
