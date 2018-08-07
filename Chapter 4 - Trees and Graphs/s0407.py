from avltree import AVLNode as BTNode
from btree import BTree as BSTree

class BTree(BSTree):
    """Binary (NOT Search) Tree"""
    def __init__(self,data = []):
        self.root = None
        self.tail = None
        super().__init__(data)

    def insert(self,key):
        return self._insert(BTNode(key))

    def _insert(self,n):
        p = self._find_tail()
        if not p:
            self.root = n
            return n
        if not p.l:
            c = 'l'
        else:
            c = 'r'
        n.parent = p
        setattr(p,c,n)
        while p:
            p.size +=1
            p = p.parent
        return n

    def _find_tail(self):
        if not self.root:
            return None
        if not self.tail or (self.tail.r and self.tail.l):
            cn = self.root
            while cn.l and cn.r:
                cn = min((cn.l.size,cn.l),(cn.r.size,cn.r))[1]
            self.tail = cn
        return self.tail


def find_common_ancestor(n1,n2):
    ancestors = set()
    for n in n1, n2:
        if not n.parent:
            return n
    while n1.parent or n2.parent:
        for n in n1, n2:
            if n.parent:
                if n.parent in ancestors:
                    return n.parent
                ancestors.add(n.parent)
                if n is n1:
                    n1 = n1.parent
                else:
                    n2 = n2.parent
    return None


#solution:
def dfs(r,n):
    if n == r:
        return True
    rl, rr = False, False
    if r.l:
        rl = dfs(r.l,n)
    if r.r:
        rr = dfs(r.r,n)
    return rl or rr

def _fca(root, searchnodes):
    if root in searchnodes:
        return root, 1
    elif not root.l and not root.r:
        return None, 0
    
    nl, nr, sl, sr = None, None, 1, 1
    if root.l:
        nl, sl =  _fca(root.l, searchnodes)
    if root.r:
        nr, sr = _fca(root.r, searchnodes)
    if nl and nr:
        return root, 2
    for n, s in (nl, sl), (nr, sr):
        if n:
            return n, s
    return None, 0

def fca(root, searchnodes):
    n, case = _fca(root, searchnodes)
    if case == 2:
        return n
    elif case == 1:
        if dfs(n,searchnodes[1 - searchnodes.index(n)]):
            return n.parent
        else:
            print('1 node in tree')
    else:
        print('0 nodes in tree')


if __name__ == '__main__':
    t = BTree([1,2,3,4])
    n5 = BTNode(5)
    t._insert(n5)
    for i in 6,7:
        t.insert(i)
    n8 = BTNode(8)
    t._insert(n8)
    for i in range(9,11):
        t.insert(i)
    n11 = BTNode(11)
    t._insert(n11)
    n12 = BTNode(12)
    t._insert(n12)
    for i in range(13,14):
        t.insert(i)
    n14 = BTNode(14)
    t._insert(n14)




    t.print()
    print(find_common_ancestor(n11,n14).key)
    print(fca(t.root,(n11,n14)).key)

    print(find_common_ancestor(n5,n8).key)
    print(fca(t.root,(n5,n8)).key)

    print(find_common_ancestor(n5,n12).key)
    print(fca(t.root,(n5,n12)).key)

