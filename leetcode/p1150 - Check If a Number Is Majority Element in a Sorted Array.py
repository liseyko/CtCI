class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return nums.count(target) > len(nums) // 2

    def isMajorityElement(self, nums, target):
        N = len(nums)
        if nums[N // 2] != target:
            return False
        lo = bisect.bisect_left(nums, target)
        hi = bisect.bisect_right(nums, target)
        return hi - lo > N // 2

    def isMajorityElement(self, nums, target):

        def search(a, x):
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) // 2
                if a[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        N = len(nums)
        if nums[N // 2] != target:
            return False
        lo = search(nums, target)
        hi = search(nums, target + 1)
        return hi - lo > N // 2
