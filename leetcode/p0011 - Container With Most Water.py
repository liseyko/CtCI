class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        maxarea = 0
        while i < j:
            maxarea = max(maxarea, (j-i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxarea

    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        lh, rh = height[i], height[j]
        res = (j-i) * min(lh, rh)
        while i < j:
            if lh < rh:
                while i < j and height[i] <= lh:
                    i += 1
                lh = height[i]
            else:
                while i < j and height[j] <= rh:
                    j -= 1
                rh = height[j]
            res = max(res, (j-i) * min(lh, rh))

        return res
