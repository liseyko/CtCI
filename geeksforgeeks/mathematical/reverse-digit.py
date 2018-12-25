import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        n = int(sys.stdin.readline())
        trim = True
        while n:
            n, d = divmod(n,10)
            if not d and trim:
                continue
            else:
                if trim:
                    trim = False
                print(d, end='')
        print()
