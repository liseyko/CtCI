from linkedlist import Node, LinkedList

class Queue(LinkedList):
    """queue implementation"""
    def __init__(self,data=[]):
        super().__init__()
        self.tail = None
        for d in data:
            self.enqueue(d)

    def enqueue(self,data):
        if self.tail:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        else:
            self.tail = Node(data)
            self.head = self.tail
        self.len += 1

    def dequeue(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = self.head
            self.len -= 1
            return data
        else:
            return None


""" Test ""
q = Queue([1,2])
print(q)
for _ in range(3):
    print(q.dequeue())

for i in range(4,7):
    q.enqueue(i)
    print(i,q,q.len)

while q.len > 0:
    print(q.dequeue(),q)

print(None == q.dequeue())
#"""