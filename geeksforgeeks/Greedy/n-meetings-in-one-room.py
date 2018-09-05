import sys

def mk_schedule(t):
    t = sorted([(t[i],str(i+1)) for i in range(len(t))])
    result = []
    pl, pr = -1, -1
    for (l, r), n in t:
        if r < pr:
            result[-1] = n
        elif l >= pr:
            result.append(n)
        else:
            continue
        pl, pr = l, r
    return ' '.join(result)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        sys.stdin.readline()
        data = list(zip(list(map(int,sys.stdin.readline().split())), \
                   list(map(int, sys.stdin.readline().split()))))
        print(mk_schedule(data))