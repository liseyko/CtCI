import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        bn = int(sys.stdin.readline())
        i = n = 0
        while bn:
            n += bn % 10 * 2 ** i
            bn //= 10
            i += 1

        print(n)