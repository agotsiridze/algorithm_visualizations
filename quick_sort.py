import matplotlib.pyplot as plt
import numpy as np


arr_length = 15
frame_time = 0.2


arr = np.random.randint(0, 100, arr_length)

x = np.arange(0, arr_length, 1)


def partition(array, low, high):
    pivot = array[high]

    i = low - 1
    for j in range(low, high):
        plt.clf()
        bar = plt.bar(x, arr)
        bar[high].set_color("green")
        if array[j] <= pivot:
            bar[j].set_color("red")
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            bar[i].set_color("yellow")
        plt.pause(frame_time)

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    plt.clf()
    plt.bar(x, arr)
    plt.pause(frame_time)

    if low < high:
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


print("Unsorted Array")
print(arr)

size = len(arr)

quickSort(arr, 0, size - 1)


print("Sorted Array in Ascending Order:")
print(arr)
plt.clf()
plt.bar(x, arr)
plt.show()
