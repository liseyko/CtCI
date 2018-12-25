import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        nums = list(map(int,sys.stdin.readline().split()))
        diff = abs(nums[0]) % abs(nums[1])

        if diff and abs(nums[1]) - 2 * diff <= 0:
            diff = diff - abs(nums[1])
        print(nums[0] // abs(nums[0]) * (abs(nums[0]) - diff))
