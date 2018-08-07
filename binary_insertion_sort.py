from random import randrange


def binary_search(arr, value, start, end):
    if start > end:
        return start
    elif start == end:
        if arr[start] > value:
            return start
        else:
            return start + 1

    mid = (start + end) // 2
    if value < arr[mid]:
        return binary_search(arr, value, start, mid)
    elif value > arr[mid]:
        return binary_search(arr, value, mid + 1, end)
    else:
        return mid


def insertion_sort(arr):
    end = len(arr)
    for i in range(1, end):
        value = arr[i]
        pos = binary_search(arr, value, 0, i - 1)
        arr = arr[:pos] + [value] + arr[pos:i] + arr[i + 1:]
    return arr


if __name__ == '__main__':
    arr = [randrange(0, 100) for i in range(10)]
    result = insertion_sort(arr)
    print(result)
