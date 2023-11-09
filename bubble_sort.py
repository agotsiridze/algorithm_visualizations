import matplotlib.pyplot as plt
import numpy as np


arr_length = 15


arr = np.random.randint(0, 100, arr_length)

x = np.arange(0, arr_length, 1)

for i in range(arr_length):
    for j in range(arr_length - i - 1):
        plt.clf()
        bars = plt.bar(x, arr)
        bars[j].set_color(c="red")
        bars[j + 1].set_color(c="green")
        plt.pause(0.2)
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

            plt.clf()
            bars = plt.bar(x, arr)
            bars[j].set_color(c="green")
            bars[j + 1].set_color(c="red")
            plt.pause(0.2)
plt.show()
