import numpy as np
import matplotlib.pyplot as plt


arr_length = 15
frame_time = 0.1


arr = np.random.randint(0, 100, arr_length)

x = np.arange(0, arr_length, 1)


for i in range(arr_length):
    min_index = i
    for j in range(min_index + 1, arr_length):
        if arr[j] < arr[min_index]:
            min_index = j
            plt.clf()
            bars = plt.bar(x, arr)
            bars[i].set_color(c="yellow")
            bars[min_index].set_color(c="green")
            plt.pause(frame_time)
        else:
            plt.clf()
            bars = plt.bar(x, arr)
            bars[i].set_color(c="yellow")
            bars[min_index].set_color(c="green")
            bars[j].set_color(c="red")
            plt.pause(frame_time)
    arr[i], arr[min_index] = arr[min_index], arr[i]
    plt.clf()
    bars = plt.bar(x, arr)
    bars[i].set_color(c="green")
    plt.pause(frame_time)
