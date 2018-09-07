import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        s = str(sys.stdin.readline().strip())
        ls = len(s)
        k, n, char2count = list(list(sys.stdin.readline().split()))
        k, n = int(k), int(n)
        r = 0

        if n <= ls:
            for i in range(n):
                if s[i] == char2count:
                    r += 1
        else:
            for c in s:
                if c == char2count:
                    r += 1
            r = (n // ls) * r
            for i in range(n % ls):
                if s[i] == char2count:
                    r += 1
        print(r)
