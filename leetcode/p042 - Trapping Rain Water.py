class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 3: return 0

        r = 0
        mxr = [h for h in height]
        
        for j in range(len(height) - 2, -1, -1):
            mxr[j] = max(mxr[j],mxr[j+1])

        mxl = height[0]
        for i in range(1,len(height)-1):
            mxl = max(mxl, height[i])
            r += min(mxl, mxr[i]) - height[i]

        return r

    def trap(self, height):
        result = 0
        l, r = 0, len(height) - 1
        lmax = rmax = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    result += lmax - height[l]
                l += 1
            else:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    result += rmax - height[r]
                r -= 1

        return result