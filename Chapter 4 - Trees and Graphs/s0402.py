import sys
from random import randint
from collections import deque

from graph import Graph


def check_route(g,s,t):
    s -= 1
    t -= 1
    if s == t:
        return True
    visited = set()
    q = deque([s])
    while q:
        u = g.vertices[q.popleft()]
        visited.add(u.id)
        for v_id in u.adj:
            if v_id in visited:
                continue
            if v_id == t:
                return True
            q.append(v_id)
    return False

if __name__ == '__main__':
    data = list(map(int,sys.stdin.read().split()))
    n, data = data[0], data[1:]
    g = Graph(n)
    g.load(data,directed=True)
    s, t = randint(1,n), randint(1,n)
    while s == t: t = randint(1,n)
    results = {False:'no', True:'a'}
    print(f'There is {results[check_route(g,s,t)]} route from {s} to {t} in graph {data}.')
