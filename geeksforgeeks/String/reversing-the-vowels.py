import sys

bvowels = {ord(c) for c in ['a','e','i','o','u']}
encoding = "latin1"

def reverse_vowels(s):
    s = bytearray(s, encoding)
    i, j = 0, len(s)-1
    while i < j:
        if s[i] not in bvowels:
            i += 1
        elif s[j] not in bvowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1
    return s.decode(encoding)

if __name__ == '__main__':
    data = list(map(str,sys.stdin.read().split()))[1:]
    for s in data:
        print(reverse_vowels(s))