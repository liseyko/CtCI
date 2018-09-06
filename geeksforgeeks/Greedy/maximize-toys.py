import sys

def knapsack(items, val):
    r = 0
    for i in sorted(items):
        val -= i
        if val > 0:
            r += 1
        else:
            return r

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        k = list(map(int,sys.stdin.readline().split()))[1]
        tc = list(map(int,sys.stdin.readline().split()))
        print(knapsack(tc, k))