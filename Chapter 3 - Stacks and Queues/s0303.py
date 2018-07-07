from stack import Stack

class SetOfStacks():
    def __init__(self,data=[],sizeOfStack=8):
        self.sizeOfStack = sizeOfStack
        #self.numberOfStacks = 1
        self.stacks = [Stack()]
        self.cur_stack = 0
        self.cur_stack_len = 0
        for d in data:
            self.push(d)

    def push(self,data):
        if self.cur_stack_len < self.sizeOfStack:
            self.stacks[self.cur_stack].push(data)
            self.cur_stack_len += 1
        else:
            self.stacks.append(Stack())
            self.cur_stack += 1
            self.cur_stack_len = 0
            self.push(data)

    def pop(self):
        data = self.stacks[self.cur_stack].pop()
        if data is None:
            return data
        self.cur_stack_len -= 1
        if self.cur_stack_len == 0 and self.cur_stack > 0:
            del(self.stacks[self.cur_stack])
            self.cur_stack -= 1
            self.cur_stack_len = len(self.stacks[self.cur_stack])
        return data

    def popAt(self,index):
        if index > self.cur_stack:
            return None
        data = self.stacks[index].pop()
        if len(self.stacks[index]) == 0 and self.cur_stack > 0:
            del(self.stacks[index])
            self.cur_stack -= 1
        return data

