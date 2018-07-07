from stack import Stack
from linkedlist import Node


class DNode(Node):
    def __init__(self,data=None,next=None,prev=None):
        self.prev = prev
        super().__init__(data,next)

class ExtendedStack(Stack):
    """ stack implementation"""
    def __init__(self,data = []):
        super().__init__(data)

    def push(self,data):
        self.head = DNode(data,self.head)
        if self.head.next is None:
            self.tail = self.head
        else:
            self.head.next.prev = self.head
        self.len += 1

    def pop(self):
        data = super().pop()
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def popBottom(self):
        data = None
        if self.tail:
            data = self.tail.data
            if self.tail.prev:
                self.tail = self.tail.prev
                #self.tail.next.prev = None
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self.len -= 1
        return data


class SetOfStacks():
    def __init__(self,data=[],sizeOfStack=8):
        self.sizeOfStack = sizeOfStack
        self.stacks = [ExtendedStack()]
        self.wasted_space = 0
        for d in data:
            self.push(d)

    def push(self,data):
        if len(self.stacks[-1]) < self.sizeOfStack:
            self.stacks[-1].push(data)
        else:
            self.stacks.append(ExtendedStack())
            self.push(data)

    def pop(self):
        data = self.stacks[-1].pop()
        if data is None:
            return data
        if len(self.stacks[-1]) == 0 and len(self.stacks) > 1:
            del(self.stacks[-1])
        return data

    def popAt(self,index):
        """optimal time, with optimisation of wasted space"""
        if index > len(self.stacks)-1:
            return None
        elif index == len(self.stacks)-1:
            return self.pop()
        data = self.stacks[index].pop()
        if len(self.stacks[index]) == 0 and len(self.stacks) > 1:
            self.wasted_space -= self.sizeOfStack
            del(self.stacks[index])
        else:
            self.wasted_space += 1
            if self.wasted_space > self.sizeOfStack * len(self.stacks) // 4 + 1:
                self.shrink() # optimize after wasting more than 25% of space
        return data

    def shiftleft(self,sl,sr):
        while len(sl) < self.sizeOfStack:
            data = sr.popBottom()
            if data is None:
                self.stacks.remove(sr)
                return False
            sl.push(data)
        if len(sr) == 0:
            self.stacks.remove(sr)
        return True

    def shrink(self):
        i = 0
        while i < len(self.stacks) - 1:
            if len(self.stacks[i]) == self.sizeOfStack:
                i += 1
                continue
            else:
                if (self.shiftleft(self.stacks[i],self.stacks[i+1])):
                    i += 1

