class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bisect(li=0, ri=len(nums)-1, nums=nums, tgt=target):
            if li > ri:
                return -1
            mi = li + (ri-li)//2
            if tgt < nums[mi]:
                return bisect(li, mi-1)
            elif tgt > nums[mi]:
                return bisect(mi+1, ri)
            return mi

        return bisect()
