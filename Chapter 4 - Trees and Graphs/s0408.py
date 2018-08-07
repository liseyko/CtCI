from collections import deque

from s0407 import BTree


def cmpT1T2(r1,r2):
    q = deque()
    q.append((r1,r2))
    while len(q) > 0:
        n1, n2 = q.popleft()
        if n1 is None and n2 is None:
            continue
        if n1.key != n2.key:
            return False
        for c in (n1.l,n2.l), (n1.r,n2.r):
            q.append(c)
    return True

def _isT1inT2(r1,r2):
    if r1.key == r2.key:
        if cmpT1T2(r1,r2):
            return True
    for c in r2.l, r2.r:
        if c and _isT1inT2(r1,c):
            return True
    return False

def isT1inT2(t1,t2):
    if t1.root is None:
        return True
    if t2.root is None:
        return False
    return _isT1inT2(t1.root,t2.root)


if __name__ == '__main__':
    t1 = BTree([i for i in range(15)])
    t1.print()

    t2 = BTree([3,7,8])
    t2.print()

    t3 = BTree([3,7,9])

    t4 = BTree([2,5,6,9,10,13,14])
    t4.print()


    print(isT1inT2(t2,t1))
    print(isT1inT2(t3,t1))
    print(isT1inT2(t4,t1))