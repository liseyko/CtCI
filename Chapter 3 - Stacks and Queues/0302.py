from linkedlist import Node, LinkedList
from random import randint
from stack import Stack

class StackMin(Stack):
    """ stack implementation"""
    def __init__(self,data = []):
        #self.min = float("inf")
        self.min = None
        self.minstack = Stack()
        super().__init__()

    def push(self,data):
        super().push(data)
        if not self.min or data <= self.min:
            self.min = data
            self.minstack.push(data)

    def pop(self):
        data = super().pop()
        if self.min == data:
            self.minstack.pop()
            self.min = self.minstack.peek()
        return data



s = StackMin()
print("pushing:\ncur_val [stack]  cur_min [min_stack]")
for _ in range(6):
    n = randint(1,24)
    s.push(n)
    print(n,s,"\t",s.min,s.minstack)
print("popping:\ncur_val [stack]  cur_min [min_stack]")
while s.len > 0:
    n = s.pop()
    print(n,s,"\t",s.min,s.minstack)
print("---")
for _ in range(6):
    n = randint(1,24)
    s.push(n)
    print(n,s,"\t",s.min,s.minstack)
print("---")
while s.len > 0:
    n = s.pop()
    print(n,s,"\t",s.min,s.minstack)
