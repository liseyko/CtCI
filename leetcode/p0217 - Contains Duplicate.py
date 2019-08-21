class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)

        return False

    def containsDuplicate(self, nums):
        return len(set(nums)) < len(nums)
