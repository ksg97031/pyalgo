def replace_spaces(str):
    arr = list(str)
    size = len(arr) + arr.count(' ') * 2
    alloc = [None] * size
    
    count = 0
    for i in arr:
        if i != ' ':
            alloc[count] = i
        else:
            alloc[count] = '%'
            alloc[count + 1] = '2'
            alloc[count + 2] = '0'
            count += 2
        count += 1

    return ''.join(alloc)

assert replace_spaces("hi a") == "hi%20a"
assert replace_spaces("hi a b c") == "hi%20a%20b%20c"
