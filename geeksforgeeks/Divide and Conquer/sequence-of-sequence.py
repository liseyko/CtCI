import sys

if __name__ == '__main__':

    cache = [[None for _ in range(201)] for _ in range(201)]
    for i in range(201):
        cache[0][i] = 0
        cache[i][0] = 0
        cache[1][i] = i
        
    for i in range(2, 201):
        for j in range(1, 201):
            r = 0
            for k in range(0, j+1):
                r += cache[i-1][(j-k)//2]
            cache[i][j] = r
    

    n = int(sys.stdin.readline())
    for _ in range(n):
        m, n = list(map(int,sys.stdin.readline().split()))
        print(cache[n][m])