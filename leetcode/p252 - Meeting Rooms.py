# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        used_rooms = 0

        start_timings = sorted([i.start for i in intervals])
        end_timings = sorted(i.end for i in intervals)
        L = len(intervals)

        end_pointer = start_pointer = 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1
            start_pointer += 1

        return used_rooms

    def minMeetingRooms(self, intervals):
        res = 0

        s = sorted([i.start for i in intervals])
        e = sorted([i.end for i in intervals])
        i = j = 0; q = len(intervals)
        while True:
            while i < q and s[i] < e[j]: 
                i += 1
            res = max(res, i - j)
            if i == q: 
                break
            while j < q and e[j] <= s[i]: 
                j += 1
        return res
    
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        idic = collections.defaultdict(int)
        for ivl in intervals:
            idic[ivl.start] += 1
            idic[ivl.end] -= 1

        max_rooms = cur_rooms = 0
        
        for t, n in sorted(idic.items()):
            cur_rooms += n
            if cur_rooms > max_rooms:
                max_rooms = cur_rooms

        return max_rooms

    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        free_rooms = []
        intervals.sort(key= lambda x: x.start)
        heapq.heappush(free_rooms, intervals[0].end)

        for i in intervals[1:]:
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)

            heapq.heappush(free_rooms, i.end)

        return len(free_rooms)