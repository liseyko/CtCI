from collections import deque

class BTNode():
    """binary tree node"""
    def __init__(self,key, parent = None):
        self.key = key
        self.l = None
        self.r = None
        self.parent = parent

class Tree():
    """binary search tree"""
    def __init__(self):
        self.root = None

    def __repr__(self):
        return self.root

    def append(self,key,node = None):
        if not node:
            if self.root:
                node = self.root
            else:
                self.root = BTNode(key)
                return True
        if key > node.key:
            if node.r:
                self.append(key, node.r)
            else:
                node.r = BTNode(key, node)
        else:
            if node.l:
                self.append(key, node.l)
            else:
                node.l = BTNode(key, node)

    def insert(self,key):
        p = self.find(key)
        n = BTNode(key)
        if not p:
            self.root = n
            return True
        
        if key > p.key:
            c = 'r'
        else:
            c = 'l'
        n.parent = p
        if getattr(p,c):
            getattr(p,c).parent = n
            n.l = getattr(p,c)
            n.r = getattr(p,c).r
        setattr(p,c,n)
        return True

    def delete(self,n):

        def appropriate_child(n):
            if n.parent.l == n:
                return "l"
            else:
                return "r"

        if not n:
            return False
        if not n.r:
            n.l.parent = n.parent
            if not n.parent:
                self.root = n.l.p
            setattr(n.parent,appropriate_child(n),n.l)
        else:
            x = self.next(n)
            while x.l:
                x = self.next(n)
            setattr(x.parent,appropriate_child(x),x.r)
            x.r.parent = x.parent
            x.l = n.l
            x.r = n.r
            x.parent = n.parent
            n.r.parent = x
            setattr(n.parent,appropriate_child(n),x)


    def find(self,key):
        n = self.root
        while n:
            if key == n.key:
                return n
            if key > n.key:
                if not n.r:
                    return n
                else:
                    n = n.r
            else:
                if not n.l:
                    return n
                else:
                    n = n.l
        return n # returns None if tree is empty

    def next(self,n = None):
        if not n:
            return n
        if n.r:
            n = n.r
            while n.l:
                n = n.l
            return n
        else:
            while n.parent and n.parent.r == n:
                n = n.parent
            return n.parent

    def range(self,l,r):
        result = []
        n = self.find(l)
        while n.key < r:
            if n.key >= l:
                result.append(n)
                n = self.next(n)
        return result

    def get_height(self,t = None):
        if t is None:
            t = self.root
            if not self.root:
                return 0
        h = 1
        for c in (t.l, t.r):
            if c is not None:
                h = max(h, 1 + self.get_height(c))
        return h

    def get_size(self, t = None):
        if t is None:
            t = self.root
            if not self.root:
                return 0
        return 1 + sum([self.get_size(c) for c in (t.l, t.r) if c is not None])

    def get_parentKey(self,n):
        if not n.parent:
            return -1
        else:
            return  n.parent.key

    def bfs(self, node = None):
        if not node:
            node = self.root
        queue = deque([node])
        result = []
        while len(queue) > 0:
            node = queue.popleft()
            #print(node.key)
            result.append(node)
            for c in node.l, node.r:
                if c:
                    queue.append(c)
        return result

    def dfs(self, node = None):
        if not node:
            node = self.root
        result = []

        if node.l:
            result += self.dfs(node.l)
        result.append(node)
        if node.r:
            result += self.dfs(node.r)
        return result


    #def rotate_right(self.node):


if __name__ == '__main__':
    t = Tree()
    for i in [5,3,8,10,7,4,1,8,13,11,12]:
        n = t.find(i)
        if n: n = n.key
        print(f'looking for {i}, found: {n}')
        #t.append(i)
        t.insert(i)

    t.delete(t.find(10))
    
    for n in t.bfs():
        print(n.key)
    print('---')

    for n in t.dfs():
        print(n.key,t.get_parentKey(n))

    print('size:', t.get_size())
    print('height:', t.get_height())

    n = t.find(0)
    while n:
        print(n.key,end=', ')
        n = t.next(n)


    print('\nrange:')
    for n in t.range(3,8):
        print(n.key, end = ', ')
