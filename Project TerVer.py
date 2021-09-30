# 2.2

import matplotlib.pyplot as plt
import random as r

# Шары
balls = ['w' for i in range(8)] + ['b' for j in range(6)] + ['r' for i in range(9)]

# Список с красными шарами
red_balls = ['r' for i in range(6)]

# Список с кол-вом проведённых испытаний
attempts = [i for i in range(1, 1600001)]

all_list = []
graph = [(0, 0)]
Q = 0  # Кол-во нужных нам вариантов исходов

# Запускаем выборку
for i in attempts:
    for j in range(6):
        xr = balls[r.randint(0, 22)]
        all_list.append(xr)

    if all_list == red_balls:
        Q += 1
    P = Q / i
    all_list = []
    graph.append((i, P))

# Строим график
x_array = []
y_array = []

for x, y in graph:
    x_array.append(x)
    y_array.append(y)
plt.plot(x_array, y_array, 'b')
plt.title('Вероятность выпадения 6 красных от выборки')
plt.show()