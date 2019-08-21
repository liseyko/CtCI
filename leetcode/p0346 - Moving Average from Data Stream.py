class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.d = collections.deque()
        self.sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.d.append(val)
        self.sum += val
        if len(self.d) > self.size:
            self.sum -= self.d.popleft()
        return self.sum / len(self.d)

class MovingAverage:
    def __init__(self, size):
        self.vect, self.sums, self.idx, self.size = [0] * size, 0, 0, size
        
    def next(self, val):
        self.idx += 1
        self.sums -= self.vect[self.idx % self.size]
        self.vect[self.idx % self.size] = val
        self.sums += val
        return self.sums / float(min(self.idx, self.size))