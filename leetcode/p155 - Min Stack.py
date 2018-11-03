class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.topMin = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.topMin = min(self.topMin, x)
        self.data.append((x, self.topMin))

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
        if self.data:
            self.topMin = self.data[-1][1]
        else:
            self.topMin = float('inf')

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()