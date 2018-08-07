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


if __name__ == '__main__':
    start, end = 0, 10
    arr = [i for i in range(end)]
    findit = randrange(start, end)
    result = binary_search(arr, findit, start, end)
    assert result == findit
