class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        g = collections.defaultdict(dict)
        for u, v, p in flights:
            g[u][v] = p

        pq = [(0, src, K+1)]
        pricemap = {}
        while pq:
            price, u, k = heapq.heappop(pq)
            if u == dst:
                return price
            if not k:
                continue
            for v, cost in g[u].items():
                #heapq.heappush(pq, (price+cost, v, k-1))
                #print(price, '+', cost, pricemap.get(v, float('inf')))
                if price+cost < pricemap.get((k, v), float('inf')):
                    pricemap[(k, v)] = price+cost
                    heapq.heappush(pq, (price+cost, v, k-1))
        return -1


class Vertex():
    def __init__(self, id):
        self.id = id
        self.adj = []
        self.wgt = {}

    def __lt__(self, other):
        return self.id < other.id


class Graph():
    def __init__(self, edges, reverseDirection=False):
        self.vertices = {}
        for (a, b, w) in edges:
            for v_id in (a, b):
                if v_id not in self.vertices:
                    self.vertices[v_id] = Vertex(v_id)
            if reverseDirection:
                self.vertices[b].adj.append(a)
                self.vertices[b].wgt[a] = w
            else:
                self.vertices[a].adj.append(b)
                self.vertices[a].wgt[b] = w


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        g = Graph(flights, reverseDirection=True)
        src, dst = dst, src
        minheap = []
        dist = {v_id: float('inf') for v_id in g.vertices}
        self.explored = set()

        heapq.heappush(minheap, (0, g.vertices[src], K))
        while minheap:
            u_dist, u, k = heapq.heappop(minheap)
            if u.id in self.explored:
                continue
            self.explored.add(u.id)
            for v_id in u.adj:
                if v_id in self.explored:
                    continue
                v = g.vertices[v_id]
                # print(u.id, '-', v.id,':', dist[v_id], 'or', u_dist, '+', u.wgt[v_id])
                if dist[v_id] > u_dist + u.wgt[v_id]:
                    dist[v_id] = u_dist + u.wgt[v_id]
                    if k:
                        heapq.heappush(minheap, (dist[v_id], v, k-1))

        return -1 if dist[dst] == float('inf') else dist[dst]
