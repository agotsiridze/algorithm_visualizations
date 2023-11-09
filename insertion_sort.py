import matplotlib.pyplot as plt
import numpy as np


arr_length = 15
frame_time = 0.5


arr = np.random.randint(0, 100, arr_length)

x = np.arange(0, arr_length, 1)


for i in range(1, arr_length):
    key = arr[i]
    j = i - 1

    plt.clf()
    plt.bar(x[:i], arr[:i], color="green")
    plt.bar(x[i:], arr[i:])
    plt.bar(x[i], arr[i], color="orange")
    plt.pause(frame_time)

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

    plt.clf()
    plt.bar(x[:i], arr[:i], color="green")
    plt.bar(x[i:], arr[i:])
    plt.bar(x[j + 1], arr[j + 1], color="orange")
    plt.pause(frame_time)

# plots
plt.clf()
plt.bar(x, arr, color="green")
plt.show()
