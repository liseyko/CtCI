class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [(None, float('-inf'))]

    def push(self, x: int) -> None:
        cur_max = self.data[-1][1]
        self.data.append((max(x, cur_max), x))

    def pop(self) -> int:
        return self.data.pop()[0]
        

    def top(self) -> int:
        return self.data[-1][0]

    def peekMax(self) -> int:
        return self.data[-1][1]

    def popMax(self) -> int:
        buf = []
        while self.data[-1][0] != self.data[-1][1]:
            buf.append(self.pop())
        cur_max = self.pop()
        while buf:
            self.push(buf.pop())
        return cur_max



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
