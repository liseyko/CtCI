class MinStack:
    def __init__(self):
        self.data = []
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.data.append(self.min)
            self.min = x
        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.min == self.data.pop():
            self.min = self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


class MinStack:
    def __init__(self):
        self.data = [(None, float('inf'))]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append((x, min(self.data[-1][1], x)))

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()

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
