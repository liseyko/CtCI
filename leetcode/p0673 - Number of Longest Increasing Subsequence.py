class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis = [1]*len(nums)
        counts = [1]*len(nums)
        ri = 0
        for pni in range(len(nums)-1):
            for cni in range(pni+1, len(nums)):
                if nums[cni] > nums[pni]:
                    if lis[pni]+1 > lis[cni]:
                        lis[cni] = lis[pni]+1
                        counts[cni] = counts[pni]
                    elif lis[pni]+1 == lis[cni]:
                        counts[cni] += counts[pni]
        maxlis = max(lis+[0])
        #print(lis, counts)
        return sum(counts[i] for i, n in enumerate(lis) if n == maxlis)

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return N
        lengths = [0] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j in range(len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
