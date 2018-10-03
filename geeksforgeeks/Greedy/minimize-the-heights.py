import sys

def mindiff(l, k):
    if len(l) < 2:
        return 0

    l.sort()

    i, j = 0, len(l)-1
    mn, mx = l[i], l[j]    

    while i <= j:
        if l[i] + k <= mx - k:
            l[i] += k
        elif l[i] - k >= mn + k:
            l[i] -= k
        else:
            if l[i] + k - mn <= mx - (l[i] - k):
                l[i] += k
            else:
                l[i] -= k
                mn = min(l[i], mn)
            sl = sorted(l)
            mn, mx = sl[0], sl[-1]
        i += 1

    l.sort()
    return l[-1] - l[0]


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        k = int(sys.stdin.readline())
        sys.stdin.readline()
        towers = list(map(int,sys.stdin.readline().split()))
        print(mindiff(towers, k))