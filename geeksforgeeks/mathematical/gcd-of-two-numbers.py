if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if b > a:
            a, b = b, a
        while b:
            a, b = b, a % b

        print(a)