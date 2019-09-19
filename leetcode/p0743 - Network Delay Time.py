class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = [[] for _ in range(N+1)]
        for u, v, w in times:
            g[u].append((w, v))
        visited = wgts = {}
        routes = [(0, K)]
        while routes:
            src_w, src = heapq.heappop(routes)
            if src in visited:
                continue
            wgts[src] = src_w
            for dst_w, dst in g[src]:
                if dst not in visited:
                    heapq.heappush(routes, (src_w+dst_w, dst))

        return max(wgts.values()) if len(visited)==N else -1
class Solution:
    ''' BFS '''
    def networkDelayTime(self, times, N, K):
        wgts = [-1]+[float("inf")] * N
        adj = [[] for _ in range(N+1)]
        q = collections.deque([(K, 0)])

        for u, v, w in times:
            adj[u].append((v, w))
            
        while q:
            u, uw = q.popleft()
            if uw < wgts[u]:
                wgts[u] = uw
                for v, vw in adj[u]:
                    q.append((v, uw + vw))
        mx = max(wgts)
        return mx if mx < float("inf") else -1


class Solution:
    ''' DFS '''
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = [[] for _ in range(N+1)]
        for u, v, w in times:
            g[u].append((w, v))
        dist = {}

        def sendPacket(src=K, ctime=0):
            dist[src] = ctime
            for t, dst in sorted(g[src]):
                if dst in dist and dist[dst] <= ctime+t:
                    continue
                sendPacket(dst, ctime+t)

        sendPacket()
        return max(dist.values()) if len(dist)==N else -1
