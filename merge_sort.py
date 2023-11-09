import matplotlib.pyplot as plt
import numpy as np


arr_length = 15
frame_time = 0.2


arr = np.random.randint(0, 100, arr_length)

x = np.arange(0, arr_length, 1)


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    plt.clf()
    plt.bar(x, arr)
    plt.pause(frame_time)

    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    merge(arr, left, right, mid)

    plt.clf()
    plt.bar(x[:mid], arr[:mid], color="lime")
    plt.bar(x[mid:], arr[mid:], color="red")
    plt.pause(frame_time)


def merge(arr, left, right, mid):
    left_cpy = arr[left : mid + 1].copy()
    right_cpy = arr[mid + 1 : right + 1].copy()

    l_counter, r_counter = 0, 0
    sorted_counter = left

    while l_counter < len(left_cpy) and r_counter < len(right_cpy):
        if left_cpy[l_counter] <= right_cpy[r_counter]:
            arr[sorted_counter] = left_cpy[l_counter]
            l_counter += 1
        else:
            arr[sorted_counter] = right_cpy[r_counter]
            r_counter += 1
        sorted_counter += 1

    while l_counter < len(left_cpy):
        arr[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
        sorted_counter += 1

    while r_counter < len(right_cpy):
        arr[sorted_counter] = right_cpy[r_counter]
        r_counter += 1
        sorted_counter += 1


print(arr)
merge_sort(arr, 0, len(arr) - 1)

print(arr)
plt.clf()
plt.bar(x, arr)
plt.show()
