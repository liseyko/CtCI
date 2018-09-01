import sys
from collections import deque

#encoding = "latin1"

def reverse_words(s, delimeter = '.'):
    #input example: i.like.this.program.very.much
    #s = bytearray(s, encoding)
    #return s.decode(encoding)
    l, r = 0, len(s)-1
    while s[l] == delimeter: l += 1
    while s[r] == delimeter: r -= 1

    result = []
    subresult = deque()
    #j = r+1
    for i in range(r, l-1, -1):
        if s[i] == delimeter:  # delimeter
            #result.append(s[i+1:j] + delimeter)
            #j = i
            subresult.append(delimeter)
            result.extend(subresult)
            subresult.clear()
            #append(s[i+1:j] + delimeter)
        else:
            subresult.appendleft(s[i])
    #result.append(s[i:j])
    result.extend(subresult)
    return ''.join(result)

        


if __name__ == '__main__':
    #print(reverse_words("i.like.this.program.very.much"))
    data = list(map(str,sys.stdin.read().split()))[1:]
    for s in data:
        print(reverse_words(s))
