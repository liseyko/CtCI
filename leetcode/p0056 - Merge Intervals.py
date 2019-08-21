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
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1, 0, -1):
            while i <= len(intervals)-1\
                  and intervals[i-1].end >= intervals[i].start:
                intervals[i-1].end = max(intervals[i-1].end, intervals[i].end)
                del intervals[i]
        return intervals

    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]] if intervals else []
        for i in range(1, len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res
