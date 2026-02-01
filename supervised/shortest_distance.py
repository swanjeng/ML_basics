import matplotlib.pyplot as plt
import random

colors = ['r', 'g', 'b']


def dis(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


# generate random dataset
x1 = [random.randint(0, 20) for _ in range(20)]
y1 = [random.randint(0, 20) for _ in range(20)]

x2 = [random.randint(20, 40) for _ in range(20)]
y2 = [random.randint(30, 50) for _ in range(20)]

x3 = [random.randint(40, 60) for _ in range(20)]
y3 = [random.randint(10, 30) for _ in range(20)]

# data point to be predicted
x = random.randint(0, 60)
y = random.randint(0, 50)

min_dis = 80
min_group = 0

for i in range(20):
    dis1 = dis(x1[i], y1[i], x, y)
    dis2 = dis(x2[i], y2[i], x, y)
    dis3 = dis(x3[i], y3[i], x, y)
    if min_dis > dis1:
        min_dis = dis1
        min_group = 1
    if min_dis > dis2:
        min_dis = dis2
        min_group = 2
    if min_dis > dis3:
        min_dis = dis3
        min_group = 3

plt.scatter(x1, y1, color='r', marker='o')
plt.scatter(x2, y2, color='g', marker='o')
plt.scatter(x3, y3, color='b', marker='o')

plt.scatter(x, y, color=colors[min_group - 1], marker='*')
plt.show()
