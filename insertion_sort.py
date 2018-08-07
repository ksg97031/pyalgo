from random import randrange


def insertion_sort(arr):
    end = len(arr)
    for i in range(1, end):
        value = arr[i]
        for j in range(0, i):
            if value < arr[j]:
                arr[j], arr[i] = value, arr[j]


if __name__ == '__main__':
    arr = [randrange(0, 10) for x in range(10)]
    insertion_sort(arr)
    print(arr)
