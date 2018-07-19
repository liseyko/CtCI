from btree import BTree

class SplayTree(BTree):
    def __init__(self,data = []):
        super().__init__(data)

    def find(self,k):
        n = super().find(k)
        if n and n.key == k:
            self.prioritize(n)
        return n

    def insert(self,k):
        n = super().insert(k)
        self.prioritize(n)
        return n


    def delete(self,n):
        p = super().delete(n)
        if p:
            self.prioritize(p)

    def prioritize(self,n):
        if not n.parent:
            return True
        ps = self.appropriate_child(n)
        if not n.parent.parent:
            self._zig(n.parent,ps)
            return True
        gps = self.appropriate_child(n.parent)
        if ps == gps:
            self._zigzig(n,ps)
        else:
            self._zigzag(n,ps,gps)
        if n.parent:
            return self.prioritize(n)
        return True

    def _zig(self,n,s):
        # rotate n.parent right if n is on a left side of his parent and vice versa
        self._rotate(n, s == "l")

    def _zigzig(self,n,s):
        self._zig(n.parent.parent, s)
        self._zig(n.parent, s)

    def _zigzag(self,n,s1,s2):
        gp = n.parent.parent
        self._zig(n.parent, s1)
        self._zig(gp, s2)



if __name__ == '__main__':
    t = SplayTree([5,3,8,10,7,4,1,8, 13,11,12])



    for n in t.bfs():
        print(n.key)
    print('---')
    print('deleting: 10')
    t.delete(t.find(10))

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


    print('\nrange 3,8:')
    for n in t.range(3,8):
        print(n.key, end = ', ')
