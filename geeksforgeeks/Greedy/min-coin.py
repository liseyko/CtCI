import sys

maxval = 1001
init_sol = [0] + [maxval] * 100000

def min_coins(val, coins):
    #coins.sort()
    sol = init_sol.copy()
    for subval in range(1, val + 1):
        for c in coins:
            if c <= subval:
                sol[subval] = min(sol[subval], sol[subval - c] + 1)
            #else:
            #    break
    return sol[val] if sol[val] != maxval else -1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for _ in range(n):
        tsum = list(map(int,sys.stdin.readline().split()))[1]
        coins = list(map(int,sys.stdin.readline().split()))
        print(min_coins(tsum, coins))
