class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        while self.q and self.q[0] <= timestamp - 300:
            self.q.popleft()

        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

class HitCounter(object):
    def __init__(self):
        self.cntr = [[0,i+1] for i in range(300)]

    def hit(self, timestamp):
        ti = int((timestamp - 1)%300)
        if self.cntr[ti][1] != timestamp:
            self.cntr[ti][:] = 0, timestamp
        self.cntr[ti][0] += 1

    def getHits(self, timestamp):
        return sum(cnt for cnt, t in self.cntr if t > timestamp - 300)
