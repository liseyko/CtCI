"""
[3,4,-1,1]

00. next = n[3-1] = -1
01. n[2] = x
10. next = n[4-1] = 1
11. n[3] = x
12. next = n[0] = 3
13. n[0] = x
14. next = n[2] == x
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """

        nl = len(nums)
        for i in range(0, nl):
            if nums[i] is not None:
                #print(nums[i], 'not None')
                next = nums[i] - 1
                while  0 <= next < nl:
                    #print(next)
                    current = next
                    next = nums[next]
                    if next is not None: next -= 1
                    nums[current] = None
                    #print(nums, current, next)
                
        #print(nums)
        for i in range(nl):
            if nums[i] is not None: 
                return i+1
        return nl + 1
