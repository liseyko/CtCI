class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        h = [(-1,-1), (-1,-1)]
        for i, n in enumerate(nums):
            heapq.heappushpop(h, (n, i))
        return h[1][1] if h[1][0]-h[0][0] >= h[0][0] else -1

    def dominantIndex(self, nums: List[int]) -> int:
        top2 = top1 = res = -1
        for i, n in enumerate(nums):
            if n > top1:
                top2, top1, res = top1, n, i
            elif n > top2:
                top2 = n
        return res if top1-top2 >= top2 else -1
