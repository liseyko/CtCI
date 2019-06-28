class MinStack:

    def __init__(self):
        self.stack = []
        self.cmin = float('inf')

    def push(self, x: int) -> None:
        self.cmin = min(self.cmin, x)
        self.stack.append((x, self.cmin))

    def pop(self) -> None:
        self.stack.pop()
        self.cmin = self.stack[-1][1] if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


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
