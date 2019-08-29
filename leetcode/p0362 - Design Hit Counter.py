class HitCounter:

    def __init__(self):
        self.q = collections.deque()
        self.cntr = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.q.append(timestamp)
        self.cntr += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        while self.q and self.q[0] <= timestamp - 300:
            self.q.popleft()
            self.cntr -= 1
        return self.cntr


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)