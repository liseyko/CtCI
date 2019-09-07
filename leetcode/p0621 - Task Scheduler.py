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
        taskCounts = list(collections.Counter(tasks).values())
        maxTask = max(taskCounts)
        maxTasksNum = taskCounts.count(maxTask)
        return max(sum(taskCounts), (maxTask-1)*(n+1)+maxTasksNum)
