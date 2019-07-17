class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(n1i):
            n2i, n3i = n1i+1, len(nums)-1
            while n2i < n3i:
                subres = [nums[n1i], nums[n2i], nums[n3i]]
                subresSum = sum(subres)
                if subresSum < 0:
                    n2i += 1
                elif subresSum > 0:
                    n3i -= 1
                else:
                    res.append(subres)
                    while n2i < n3i and nums[n2i] == nums[n2i+1]:
                        n2i += 1
                    while n2i < n3i and nums[n3i] == nums[n3i-1]:
                        n3i -= 1
                    n2i, n3i = n2i + 1, n3i - 1

        for n1i in range(len(nums)-2):
            if nums[n1i] > 0:
                break
            if n1i and nums[n1i-1] == nums[n1i]:
                continue
            twoSum(n1i)

        return res
