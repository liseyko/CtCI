import sys

def modexp(a, b, c):
    r = 1
    for _ in range(b):
        r = ((r % c) * (a % c)) % c;
    return r


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, b, c = list(map(int,sys.stdin.readline().split()))
        print(modexp(a, b, c))