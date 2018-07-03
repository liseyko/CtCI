from linkedlist import LinkedList

class LL(LinkedList):
    def __init__(self,head=None):
        super().__init__(head)

    def undupe(self):
        buffer = set()
        n = self.head
        if n:
            buffer.add(n.data)
        else:
            return
        while n.next:
            if n.next.data not in buffer:
                buffer.add(n.next.data)
                n = n.next
            else:
                n.next = n.next.next

    def undupe_slow(self):
        buffer = set()
        i = self.head
        if not i:
            return
        while i:
            j = self.head
            while j.next:
                if j.next.data == i.data and i != j.next:
                    j.next = j.next.next
                else:
                    j = j.next
            i = i.next


ll1 = LL()
ll1.populate(16,8)
ll1.print_data()
ll1.undupe_slow()
ll1.print_data()