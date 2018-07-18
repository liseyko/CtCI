from collections import deque

class TNode():
    def __init__(self,key):
        self.key = key
        self.children = []

class BTNode():
    """binary tree node"""
    def __init__(self,key, parent = None):
        self.key = key
        self.l = None
        self.r = None
        self.parent = parent

class BTree():
    """binary search tree"""
    def __init__(self):
        self.root = None

    def insert(self,key):
        return self._insert(BTNode(key))

    def _insert(self,n):
        p = self.find(n.key)

        if not p:
            self.root = n
            return n
        
        if n.key > p.key:
            c = 'r'
        else:
            c = 'l'
        n.parent = p
        if getattr(p,c):
            getattr(p,c).parent = n
            n.l = getattr(p,c)
            n.r = getattr(p,c).r
        setattr(p,c,n)
        return n

    def appropriate_child(self,c,p = None):
        if not p:
            p = c.parent
        if p.l and p.l == c:
            return "l"
        elif p.r and p.r == c:
            return "r"
        else:
            return None

    def delete(self,n):
        if not n:
            return False
        if not n.r:
            if n.l:
                n.l.parent = n.parent
            elif not n.parent:
                self.root = None
            setattr(n.parent,self.appropriate_child(n),n.l)
            return(n.parent)
        else:
            x = self.next(n)
            while x.l:
                x = self.next(n)
            setattr(x.parent,self.appropriate_child(x),x.r)
            if x.r:
                x.r.parent = x.parent
            x.l = n.l
            x.r = n.r
            x.parent = n.parent
            if n.r:
                n.r.parent = x
            setattr(n.parent,self.appropriate_child(n),x)
            return(x.parent)

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
            if not self.root:
                return 0
            t = self.root
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

    def print(self):
        n = self.root
        if not n: return
        queue = deque([n])
        i, lvl = 0, 0
        done = True
        for j in range(10):
            print('  ',end = '  ')

        while len(queue) > 0:
            n = queue.popleft()
            if n:
                done = False
                if n.parent: pk = n.parent.key
                else: pk = -1
                print(f'{n.key}', end='  ')
                for c in n.l, n.r:
                    queue.append(c)
            else:
                print('__', end='  ')
                for _ in range(2):
                    queue.append(None)
            i+=1
            if i == 2 ** lvl:
                print("\n")
                for j in range(10-(2 ** lvl)//2):
                   print('  ',end = '  ')
                if done:
                    break
                done = True
                lvl += 1
                i = 0
        print()


    def bfs(self, node = None):
        if not node:
            node = self.root
        queue = deque([node])
        result = []
        while len(queue) > 0:
            node = queue.popleft()
            #print(node.key)
            result.append(node)
            for n in node.l, node.r:
                if n:
                    queue.append(n)
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

    def _rotate(self,x,right = True):
        if right:
            fwd_dir, bwd_dir = "r", "l"
        else:
            fwd_dir, bwd_dir = "l", "r"
        if not getattr(x,bwd_dir):
            print(f'no {bwd_dir} rotation possible for {x.key}')
            return False
        p = x.parent
        y = getattr(x,bwd_dir)
        b = getattr(y,fwd_dir)
        x.parent = y
        y.parent = p
        setattr(x,bwd_dir,b)
        setattr(y,fwd_dir,x)
        if b:
            b.parent = x
        if p:
            setattr(p,self.appropriate_child(x,p),y)
        else:
            self.root = y

    def rotateRight(self,x):
        self._rotate(x)

    def rotateLeft(self,x):
        self._rotate(x, False)

    def parentKey(self,n):
        if not n.parent:
            return -1
        else:
            return  n.parent.key

    def key(self,n):
        if not n:
            return -1
        else:
            return n.key






if __name__ == '__main__':
    t = BTree()
    for i in [5,3,8,10,7,4,1,8,13,11,12]:
        #n = t.find(i)
        #if n: n = n.key
        #print(f'looking for {i}, found: {n}')
        #t.append(i)
        t.insert(i)
        #t.avlInsert(i)


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
