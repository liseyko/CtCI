class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cmin = float('inf')
        cmax = res = float('-inf')
        for a in arrays:
            res = max(res, max(cmax-a[0], a[-1]-cmin))
            cmin, cmax = min(cmin, a[0]), max(cmax, a[-1])
        return res

    def maxDistance(self, arrays: List[List[int]]) -> int:
        n, m = [(float('-inf'), -1)]*2, [(float('-inf'), -1)]*2
        for i, l in enumerate(arrays):
            heapq.heappushpop(n, (-l[0], i))
            heapq.heappushpop(m, (l[-1], i))

        if n[1][1] != m[1][1]:
            return m[1][0]+n[1][0]
        else:
            return max(m[0][0]+n[1][0], m[1][0]+n[0][0])
