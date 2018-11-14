# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start)
        for i in range(len(intervals) - 1, 0, -1):
            while i <= len(intervals)-1 and intervals[i-1].end >= intervals[i].start:
                intervals[i-1].end = max(intervals[i-1].end, intervals[i].end)
                del intervals[i]
                
        return intervals
    
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged