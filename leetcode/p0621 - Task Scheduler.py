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


    def leastInterval(self, tasks: List[str], N: int) -> int:
        """ https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation """
        task_counts = list(collections.Counter(tasks).values())
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)
