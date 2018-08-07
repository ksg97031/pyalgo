from random import randrange


def partition(arr, start, end):
    pivot_index = randrange(start, end + 1)
    pivot_value = arr[pivot_index]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    temp_index = start
    for i in range(start, end):
        if arr[i] < pivot_value:
            arr[i], arr[temp_index] = arr[temp_index], arr[i]
            temp_index += 1

    arr[end], arr[temp_index] = arr[temp_index], arr[end]
    return temp_index


def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


if __name__ == '__main__':
    for i in range(10):
        arr = [randrange(0, 11) for x in range(100)]
        arr_copy = list(arr)
        quick_sort(arr, 0, len(arr) - 1)
        print(arr)
