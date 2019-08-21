class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStk, self.outStk = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStk.append(x)

    def _refillOutOnDemand(self):
        if self.outStk:
            return
        while self.inStk:
            self.outStk.append(self.inStk.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self._refillOutOnDemand()
        return self.outStk.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._refillOutOnDemand()
        return self.outStk[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.outStk or self.inStk)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
