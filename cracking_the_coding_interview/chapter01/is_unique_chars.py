from string import ascii_lowercase

# character range in 'a' ~ 'z'
def is_unique_chars(s):
    checker= 0
    for c in list(map(ord, s)):
        bit_pos = c - 97
        val = 1 << bit_pos
        if checker & val == val:
            return False
        checker |= val
    return True

assert is_unique_chars(ascii_lowercase)
assert not is_unique_chars(ascii_lowercase + "z")
