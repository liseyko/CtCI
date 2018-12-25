if __name__ == '__main__':
    for _ in range(int(input())):
        if int(input()) < 2:
            print(int(input()))
            continue
        nums = sorted(map(int, input().split()))

        while len(nums) > 1:
            nums = [nums[i] % nums[0] for i in range(1, len(nums))
                    if nums[i] % nums[0]] + [nums[0]]
        print(*nums)
