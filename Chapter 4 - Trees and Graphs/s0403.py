class BTNode():
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

class BTree():
    def __init__(self):
        self.root = None

    def _intArray2BTree(self,intlist,l,r):
        m = (l + r) // 2
        n = BTNode(intlist[m])
        if l < m:
            n.l = self._intArray2BTree(intlist,l,m-1)
        if m < r:
            n.r = self._intArray2BTree(intlist,m+1,r)
        return n
        
    def loadFromSortedIntArray(self,intlist):
        if intlist:
            self.root = self._intArray2BTree(intlist,0,len(intlist)-1)

"""
perfect case:
[l,2,3,m,5,6,r]
less perfect case:
[l,2,m,4,5,r]
base:
[l,2,m,4,r]
[l,m,3,r]
[l,m,r]
"""

if __name__ == '__main__':

    t= BTree()

    t.loadFromSortedIntArray([1,2,3,4,5,6,7])
    print(t.root.data)
    print(t.root.l.data, t.root.r.data)
    print(t.root.l.l.data, t.root.l.r.data,t.root.r.l.data, t.root.r.r.data)
    print()
    t.loadFromSortedIntArray([1,2,3,4,5,6])
    print(t.root.data)
    print(t.root.l.data, t.root.r.data)
    print(t.root.l.r.data, t.root.r.l.data, t.root.r.r.data)
    print()
    t.loadFromSortedIntArray([1,2,3,4,5])
    print(t.root.data)
    print(t.root.l.data, t.root.r.data)
    print(t.root.l.r.data, t.root.r.r.data)
    print()
    t.loadFromSortedIntArray([1,2,3,4])
    print(t.root.data)
    print(t.root.l.data, t.root.r.data)
    print(t.root.r.r.data)
    print()
    t.loadFromSortedIntArray([1,2])
    print(t.root.data)
    print(t.root.r.data)
    print()
    t.loadFromSortedIntArray([2])
    print(t.root.data)

