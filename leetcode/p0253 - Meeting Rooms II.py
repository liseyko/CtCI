class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        h = []
        res = cur = 0
        for tf in sorted(intervals):
            while h and h[0] <= tf[0]:
                heapq.heappop(h)
                cur -= 1
            heapq.heappush(h, (tf[1]))
            cur += 1
            res = max(res, cur)
        return res

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''1st try'''
        h = []
        res = cur = 0
        for tf in intervals:
            heapq.heappush(h, (tf[0], 1))
            heapq.heappush(h, (tf[1], -1))
        while h:
            cur += heapq.heappop(h)[1]
            res = max(res, cur)
        return res
