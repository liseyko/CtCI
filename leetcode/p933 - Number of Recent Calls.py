from collections import deque

class RecentCounter:

    def __init__(self):
        self.log = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.log.append(t)
        if t > 3000:
            while self.log[0] < t - 3000:
                self.log.popleft()
                
        return len(self.log)

rc = RecentCounter()
print(rc.ping(1))
print(rc.ping(100))
print(rc.ping(3001))
print(rc.ping(3002))