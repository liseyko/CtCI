import sys

def mk_schedule(t):
    result = 0
    pl, pr = -1, -1
    for l, r in sorted(t):
        if l >= pr:
            result += 1
        elif r < pr:
            pass
        else:
            continue
        pl, pr = l, r
    return result

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        sys.stdin.readline()
        data = list(zip(list(map(int,sys.stdin.readline().split())), \
                   list(map(int, sys.stdin.readline().split()))))
        print(mk_schedule(data))