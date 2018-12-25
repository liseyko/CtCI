import sys

if __name__ == '__main__':
    primes = [i for i in range(2, 50000+1)]
    for i, n in enumerate(primes):
        if n:
            for j in range(i+n, len(primes), n):
                primes[j] = None
    primes = [n for n in primes if n]

    input = list(map(int, sys.stdin.read().split()))[1:]
    for i in input:
        factors = [1] + [p for p in primes if p < i and not i % p]
        print(int(sum(factors) == i))
