import os

os.system('cls')


def get_fragment(string, n):
    result = ''
    if n == 1:
        return string[0]
    else:
        for i in range(n-1):
            result = result + string[i]
        secont_pt = string[n-1::-1]
        result += secont_pt
    return result


s = 'abcdefghijklmnop'

assert get_fragment(s, 1) == "a"
assert get_fragment(s, 2) == "aba"
assert get_fragment(s, 3) == "abcba"
assert get_fragment(s, 4) == "abcdcba"
