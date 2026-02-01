import matplotlib.pyplot as plt
import random

colors = ['r', 'g', 'b']

K = 5


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


distances = []
for i in range(20):
    distance = dis(x1[i], y1[i], x, y)
    distances.append((distance, 1))
    distance = dis(x2[i], y2[i], x, y)
    distances.append((distance, 2))
    distance = dis(x3[i], y3[i], x, y)
    distances.append((distance, 3))

distances.sort()
cnt = [0, 0, 0]
for i in range(K):
    cnt[distances[i][1] - 1] += 1

min_group = cnt.index(max(cnt))


plt.scatter(x1, y1, color='r', marker='o')
plt.scatter(x2, y2, color='g', marker='o')
plt.scatter(x3, y3, color='b', marker='o')
plt.scatter(x, y, color=colors[min_group], marker='*')
plt.show()
