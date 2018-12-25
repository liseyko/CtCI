if __name__ == '__main__':
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if b > a:
            a, b = b, a
        gcd, divisor = a, b
        while divisor:
            gcd, divisor = divisor, gcd % divisor

        print(a * b // gcd, gcd)