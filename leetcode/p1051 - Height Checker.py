class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        sh = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sh[i]:
                res += 1
        return res
