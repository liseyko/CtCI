import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        nums = list(map(int,sys.stdin.readline().split()))
        n = int(sys.stdin.readline())
        print(nums[0]+(nums[1]-nums[0])*(n-1))