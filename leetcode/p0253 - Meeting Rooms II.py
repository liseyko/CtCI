class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        res = cur = 0
        for tf in intervals:
            heapq.heappush(h, (tf[0], 1))
            heapq.heappush(h, (tf[1], -1))
        while h:
            cur += heapq.heappop(h)[1]
            res = max(res, cur)
        return res
