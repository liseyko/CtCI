from linkedlist import Node, LinkedList

class Stack(LinkedList):
    """ stack implementation"""
    def __init__(self,data = []):
        super().__init__()
        #self.top = None
        for d in data:
            self.push(d)

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self.len -= 1
            return data
        else:
            return None

    def push(self,data):
        self.head = Node(data,self.head)
        self.len += 1

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

""" Test ""
stack = Stack([1,2,3])
print(len(stack),stack)

for i in range(4,7):
    stack.push(i)
    print(i,stack)

while stack.len > 0:
    print(stack.pop(),stack)

print(None == stack.pop())
#"""