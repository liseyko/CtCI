class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1, self.q2 = self.q2, self.q1
        self.q1.appendleft(x)
        while self.q2:
            self.q1.appendleft(self.q2.pop())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
