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
