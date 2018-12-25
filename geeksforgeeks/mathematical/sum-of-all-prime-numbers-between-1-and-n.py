import sys

if __name__ == '__main__':
    input = list(map(int, sys.stdin.read().split()))[1:]
    primes = [i for i in range(2, max(input)+1)]
    for i, n in enumerate(primes):
        if n:
            for j in range(i+n, len(primes), n):
                primes[j] = None
    primes = [n for n in primes if n]
    for i in input:
        print(sum([p for p in primes if p <= i]))
