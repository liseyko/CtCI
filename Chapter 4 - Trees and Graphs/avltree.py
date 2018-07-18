from collections import deque

from btree import BTree, BTNode

class AVLNode(BTNode):
    """Node for LVM tree"""
    def __init__(self,key):
        super().__init__(key)
        self.height = 1
        self.size = 1

class AVLTree(BTree):
    """binary search tree"""
    def __init__(self):
        super().__init__()

    def insert(self,key):
        self.rebalance(super()._insert(AVLNode(key)))

    def delete(self,n):
        n = super().delete(n)
        if n:
            self.rebalance(n)


    def _rebalanceLorR(self, n, right = True):
        if right:
            c = "l"
        else: 
            c = "r"
        m = getattr(n,c)

        lh = self.height(m.l)
        rh = self.height(m.r)
        if (lh - rh < 0 and right) or (lh - rh > 0 and not right):
            self._rotate(m, not right)
        self._rotate(n,right)


    def _rebalanceRight(self, n):
        self._rebalanceLorR(n)

    def _rebalanceLeft(self, n):
        self._rebalanceLorR(n, False)

    def rebalance(self,n):
        p = n.parent
        lh = self.height(n.l)
        rh = self.height(n.r)
        if lh - rh > 1:
            self._rebalanceRight(n)
        elif lh - rh < -1:
            self._rebalanceLeft(n)
        self.adjustHeight(n)
        if p:
            self.rebalance(p)

    def appropriate_child(self,c,p = None):
        if not p:
            p = c.parent
        if p.l and p.l == c:
            return "l"
        elif p.r and p.r == c:
            return "r"
        else:
            return None

    def adjustHeight(self, n):
        while n is not None:
            n.height = 1 + max(self.height(n.l),self.height(n.r))
            n = n.parent

    def height(self,n):
        if not n:
            return 0 
        return n.height



if __name__ == '__main__':
    t = AVLTree()
    for i in [5,3,8,10,7,4,1,8,13,11,12]:
        #n = t.find(i)
        #if n: n = n.key
        #print(f'looking for {i}, found: {n}')
        #t.append(i)
        #t.insert(i)
        t.insert(i)


    ### t.rotateRight(t.find(5))
    #print("deleting 10")
    t.delete(t.find(10))


    
    for n in t.bfs():
        print(n.key)
    print('---')

    t.print()

    print('---')

    for n in t.dfs():
        print(n.key,t.parentKey(n))

    print('size:', t.get_size())
    print('height:', t.get_height())

    n = t.find(0)
    while n:
        print(n.key,end=', ')
        n = t.next(n)


    print('\nrange:')
    for n in t.range(3,8):
        print(n.key, end = ', ')
