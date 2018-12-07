class Solution:
    
    def findMinArrowShots(self, points):
        points.sort()
        if not points: return 0
        res = 1
        cur = [float('-inf'),float('inf')]
        for p in points:
            cur[0], cur[1] = max(cur[0], p[0]), min(cur[1], p[1])
            if cur[0] > cur[1]:
                cur = p
                res += 1
        return res

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key = lambda x: x[1])
        res, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res    