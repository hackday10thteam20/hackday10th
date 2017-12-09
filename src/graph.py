import numpy as np
from matplotlib import pyplot as plt

# 配列
t = np.zeros(100)
y = np.zeros(100)
time = 0
result = 0

#インタラクティブ描画
plt.ion()
plt.figure()
li, = plt.plot(t, y)
plt.ylim(0, 100)
plt.xlabel("time[s]")
plt.ylabel("score")

while True:
    try:
        # 配列をキューと見たてて要素を追加・削除
        t = np.append(t, time)
        t = np.delete(t, 0)
        print(t)
        y = np.append(y, result)
        y = np.delete(y, 0)

        li.set_xdata(t)
        li.set_ydata(y)           
        plt.xlim(min(t), max(t))
        plt.draw()

        time += 1
        result += 1
        plt.pause(1)
    except KeyboardInterrupt:
        break

