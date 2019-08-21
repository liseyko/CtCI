class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = collections.defaultdict(int)
        start, end = {}, {}

        for i, n in enumerate(nums):
            freq[n] += 1
            end[n] = i
            if n not in start:
                start[n] = i

        degree = max(freq.values())
        res = len(nums)

        for n, f in freq.items():
            if f == degree:
                res = min(res, end[n] + 1 - start[n])

        return res
