import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        nums = list(map(int,sys.stdin.readline().split()))
        n = int(sys.stdin.readline())
        mul = nums[1] / nums[0]
        for _ in range(1,n):
            nums[0] *= mul

        print(int(nums[0]))