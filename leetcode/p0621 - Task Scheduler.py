class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = cooldown = 0
        td = collections.Counter(tasks)
        h = [-v for v in td.values()]
        heapq.heapify(h)
        while h:
            res += cooldown
            cooldown = n+1
            buf = []
            while h and cooldown:
                v = - heapq.heappop(h)-1
                if v:
                    buf.append(-v)
                res += 1
                cooldown -= 1
            while buf:
                heapq.heappush(h, buf.pop())
        return res
