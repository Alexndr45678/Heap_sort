import random


def heap_sort(array):
    build_max(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, index=0, size=i)


def parent_index(i):
    return (i - 1) // 2


def left_element(i):
    return 2 * i + 1


def right_element(i):
    return 2 * i + 2


def build_max(array):
    length = len(array)
    start = parent_index(length - 1)
    while start >= 0:
        max_heapify(array, index=start, size=length)
        start -= 1


def max_heapify(array, index, size):
    l = left_element(index)
    r = right_element(index)
    if l < size and array[l] > array[index]:
        largest = l
    else:
        largest = index
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        max_heapify(array, largest, size)


array = [random.randint(0, 50) for i in range(20)]
print("Неотсортированный список", array)
heap_sort(array)
print("Отсортированный список:", array)
