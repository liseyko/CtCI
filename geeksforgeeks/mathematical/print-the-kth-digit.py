import sys

if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        nums = list(map(int,sys.stdin.readline().split()))
        #r = nums[0]**nums[1]
        r = 1
        limit = 10 ** nums[2]
        for _ in range(nums[1]):
            r = r * nums[0] % limit
        #print(r % 10 ** nums[2] // 10 ** (nums[2]-1))
        print(r // 10 ** (nums[2]-1))