class Solution:
    ''' Dijkstra '''
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        g = [[] for _ in range(N+1)]
        for u, v, w in times:
            g[u].append((w, v))
        dist = {}
        routes = [(0, K)]
        while routes:
            src_dist, src = heapq.heappop(routes)
            if src in dist:
                continue
            dist[src] = src_dist
            for dst_dist, dst in g[src]:
                if dst not in dist:
                    heapq.heappush(routes, (src_dist+dst_dist, dst))

        return max(dist.values()) if len(dist)==N else -1

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
        #print(vis) 
        return max(dist.values()) if len(dist)==N else -1
