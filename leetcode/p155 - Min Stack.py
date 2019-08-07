class MinStack:

    def __init__(self):
        self.stack = [(None, float('inf'))]

    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        if len(self.stack) > 1:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
