from collections import deque
from random import randint

from s0407 import BTree


def get_sum(node, value):
    if not node or value < node.key:
        return None
    if value == node.key:
        return [[node.key]]
    if not node.l and not node.r:
        return None
    result = []
    for c in node.l, node.r:
       if c:
           subsums = get_sum(c, value - node.key)
           if subsums:
               for subsum in subsums:
                   result.append([node.key] + subsum)
    if result:
       return result
    return None

def bfs_sums(t,val):
    if not t.root:
        return None
    results = []
    q = deque([t.root])
    while len(q) > 0:
        n = q.popleft()
        s = get_sum(n,val)
        if s:
            results.append(s)
        for c in n.l, n.r:
            if c:
                q.append(c)
    return results


def printPath(path, start, end):
    for i in range(start,end+1):
        print(path[i], end=' ')
    print()

def _depth(node):
    if not node:
        return 0
    return 1 + max(_depth(node.l), _depth(node.r))

def _findSum(node,sum,path,level):
    if not node:
        return
    path[level] = node.key

    t = 0
    for i in range(level,-1,-1):
        t += path[i]
        if t == sum:
            printPath(path, i, level)

    for c in node.l, node.r:
        if c:
            _findSum(c, sum, path, level+1)

    path[level] = float('-inf')


def findSum(t,sum):
    node = t.root
    if not node:
        return
    depth = _depth(node)
    path = [_ for _ in range(depth)]
    return _findSum(node, sum, path,0)


if __name__ == '__main__':
    t = BTree([randint(1,9) for _ in range(31)])
    t.print()
    print(bfs_sums(t,14))
    findSum(t,14)