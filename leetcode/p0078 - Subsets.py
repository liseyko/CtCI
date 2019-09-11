class Solution:
    def subsets(self, nums):
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res


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

    def subsets(self, nums: List[int]) -> List[List[int]]:

        def bt(i=0, buf=[]):
            self.res.append(buf[:])
            for j in range(i, len(nums)):
                bt(j+1, buf+[nums[j]])

        self.res = []
        bt()
        return self.res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for mask in range(2**len(nums)):
            curSet = []
            for bit in range(len(nums)):
                if mask & 1 << bit:
                    curSet.append(nums[bit])
            res.append(curSet)
        return res
