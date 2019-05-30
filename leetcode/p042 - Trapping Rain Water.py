class Solution(object):

    def trap(self, height):
        lmax = rmax = res = 0
        li, ri = 0, len(height)-1
        while li <= ri:
            if lmax < rmax:
                lmax = max(lmax, height[li])
                res += lmax - height[li]
                li += 1
            else:
                rmax = max(rmax, height[ri])
                res += rmax - height[ri]
                ri -= 1
        return res

    def trap(self, height):
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water

    def trap(self, height: List[int]) -> int:
        result = limL = limR = 0
        i, j = 0, len(height) - 1
        while i <= j:
            if height[i] < height[j]:
                result += max(0, limL - height[i])
                limL = max(limL, height[i])
                i += 1
            else:
                result += max(0, limR - height[j])
                limR = max(limR, height[j])
                j -= 1

        return result
