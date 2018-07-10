from stack import Stack
from queue import Queue

class MyQueue():
    """queue implementation using 2 stacks"""
    def __init__(self):
        self.old_stack = Stack()
        self.new_stack = Stack()

    def enqueue(self,data):
        self.new_stack.push(data)

    def dequeue(self):
        if len(self.old_stack) > 0:
            return self.old_stack.pop()
        else:
            while len(self.new_stack) > 1:
                self.old_stack.push(self.new_stack.pop())
            return self.new_stack.pop()

    def __str__(self):
        return str(self.old_stack) + str(self.new_stack)
