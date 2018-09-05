import sys

def min_sum(sums):
    s0 = sorted(list(map(int,sums[0].split())))
    s1 = sorted(list(map(int,sums[1].split())), reverse = True)
    minsum = 0
    for i in range(len(s0)):
        minsum += s0[i] * s1[i]
    return minsum

if __name__ == '__main__':
    data = list(map(str,sys.stdin.read().split("\n")))
    data = list(zip(data[2::3], data[3::3]))
    for s in data:
        print(min_sum(s))