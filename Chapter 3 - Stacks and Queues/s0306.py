from stack import Stack

class SortedStack():
    """ascending order # with biggest item on top"""
    def __init__(self):
        self.size = 0
        self.stack = Stack()
        self.buffer = Stack()

    def push(self,data):
        if self.isEmpty():
            self.stack.push(data)
        else:
            while len(self.stack) > 0 and self.peek() > data:
                self.buffer.push(self.stack.pop())
            self.stack.push(data)
            while len(self.buffer) > 0:
                self.stack.push(self.buffer.pop())
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            self.size -= 1
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def isEmpty(self):
        if self.size ==-0:
            return True
        else:
            return False

    def __str__(self):
        l = []
        n=self.stack.head
        while n:
            l.append(n.data)
            n = n.next
        return str(l)
