import sys

def get_last(a):
    i, j = 0, len(a)-1
    while i < j:
            if a[i] > a[j]:
                i += 1
            else:
                j -= 1
    return a[i]
        

if __name__ == '__main__':
    data = list(map(str,sys.stdin.read().split("\n")))[2::2]
    for s in data:
        print(get_last(list(map(int,s.split()))))