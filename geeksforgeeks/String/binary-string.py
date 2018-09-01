import sys

def n_of_substr(s,tpl='1'):
    #actually, it's basic combinatorics:
    i=0
    for d in s:
        if d == tpl:
            i += 1
    return i*(i-1)//2

if __name__ == '__main__':
    data = list(map(str,sys.stdin.read().split()))[2::2]
    for s in data:
        print(n_of_substr(s))