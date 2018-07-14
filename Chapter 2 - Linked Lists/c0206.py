""" given circular linked list, 
    implement an algorithm which 
    returns the node at the beginning of the loop 
    [definition] circular linked list: A corrupt linked list
    in which  a node's next pointer points to an earlier node, so as to make a loop in the linled list
"""

from linkedlist import LinkedList
from random import randint

class LL(LinkedList):

    def __init__(self,lst = []):
        super().__init__(lst)

    def findLoop_naive(self):
        buffer = set()
        for n in self:
            if n in buffer:
                return n
            else:
                buffer.add(n)
        return None

    def findLoop0(self):
        turtle = self.head
        if turtle and turtle.next:
            rabbit = turtle.next
        else:
            return None
        while rabbit:
            for _ in range(100):
                if rabbit:
                    rabbit = rabbit.next
                if rabbit == turtle:
                    return turtle
            turtle = turtle.next
        return None

    def findLoop(self):
        turtle = self.head
        if turtle and turtle.next:
            rabbit = turtle
        else:
            return None

        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if rabbit == turtle:
                break

        if not rabbit or not rabbit.next:
            return None

        turtle = self.head
        while turtle != rabbit:
            turtle = turtle.next
            rabbit = rabbit.next

        return rabbit


    def addSomeLoop(self):
        t = randint(1,self.len//2)
        n = self.head
        target_node = n
        #print(self.len,t)
        for i in range(randint(self.len // 2+1,self.len-1)):
            if i == t:
                target_node = n
                print("loop element:",t,"(",n.data,")")
            n = n.next
        n.next = target_node
        #print('\n',i+1,'=>',t,'[',n.data,'=>',target_node.data,']')


l1 = LL()
l1.populate(16)
l1.mkunique()
print(l1)
l1.addSomeLoop()
loop = l1.findLoop_naive()
loop2 = l1.findLoop()
if loop:
    print(loop.data)
else:
    print("no loops has been found")

if loop2:
    print(loop2.data)
else:
    print("no loops has been found")
