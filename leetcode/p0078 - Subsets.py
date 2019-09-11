class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def bt(i=0, buf=[]):
            if i == len(nums):
                self.res.append(buf[:])
                return
            bt(i+1, buf)
            bt(i+1, buf+[nums[i]])

        self.res = []
        bt()
        return self.res
