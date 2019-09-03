class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        return (self.nums[(len(self.nums)-1) // 2] +
                self.nums[len(self.nums) // 2]) / 2


class MedianFinder:

    def __init__(self):
        self.minh, self.maxh = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minh, num)
        heapq.heappush(self.maxh, -heapq.heappop(self.minh))
        if len(self.minh) < len(self.maxh):
            heapq.heappush(self.minh, -heapq.heappop(self.maxh))

    def findMedian(self) -> float:
        return self.minh[0] if len(self.minh) > len(self.maxh) else\
               (self.minh[0] - self.maxh[0]) / 2
