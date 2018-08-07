from random import randrange


def merge(left_block, right_block):
    temp = []
    left_index = right_index = 0
    left_block_len, right_block_len = len(left_block), len(right_block)

    while left_index != left_block_len and right_index != right_block_len:
        if left_block[left_index] < right_block[right_index]:
            temp.append(left_block[left_index])
            left_index += 1
        else:
            temp.append(right_block[right_index])
            right_index += 1

    if left_index != left_block_len:
        temp += left_block[left_index:]
    else:
        temp += right_block[right_index:]

    return temp


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_block = merge_sort(arr[:mid])
        right_block = merge_sort(arr[mid:]) 
        return merge(left_block, right_block)
    return arr


if __name__ == '__main__':
    arr = [randrange(0, 10) for x in range(10)]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
