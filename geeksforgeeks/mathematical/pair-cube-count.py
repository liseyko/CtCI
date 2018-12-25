import sys

if __name__ == '__main__':

    input = list(map(int, sys.stdin.read().split()))[1:]
    cubes = [i**3 for i in range(1,int(10**5/3)+1)]
    for n in input:
        cntr = 0
        for a in cubes:
            if a >= n:
                if a == n:
                    cntr += 1 
                break
            else:
                for b in cubes:
                    if b >= n - a:
                        if b == n-a:
                            cntr += 1
                        break
        print(cntr)
