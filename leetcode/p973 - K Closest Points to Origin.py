class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = [(float('-inf'), None)] * K

        for p in points:
            dist = p[0]**2 + p[1]**2  # math.sqrt(p[0]**2 + [1]**2)
            heapq.heappushpop(h, (-dist, p))

        return [p for _, p in h]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return heapq.nsmallest(K, points, key = lambda xy: xy[0]**2 + xy[1]**2)
