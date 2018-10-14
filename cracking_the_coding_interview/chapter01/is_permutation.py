def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(list(str1)) == sorted(list(str2))

assert is_permutation("dog", "god")
assert not is_permutation("dog", "goda")
assert not is_permutation("dog", "goe")

def is_permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    
    arr = [0 for x in range(128)] # only support ascii chars not unicode
    for c in str1: arr[ord(c)] += 1
    for c in str2: 
        ascii_c = ord(c)
        arr[ascii_c] -= 1
        if arr[ascii_c] < 0:
            return False

    return True

assert is_permutation2("dog", "god")
assert not is_permutation2("dog", "goda")
assert not is_permutation2("dog", "goe")
