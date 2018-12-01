from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1, self.q2 = deque(), deque()
        self.top_element = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.top_element = x
        self.q1.appendleft(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        i = 0
        while self.q1:
            res = self.q1.pop()
            if self.q1:
                self.top_element = res
                self.q2.appendleft(res)
        self.q1, self.q2 = self.q2, deque()
        if not self.q1: 
            self.top_element = None
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_element
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q1) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()