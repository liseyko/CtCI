class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        unprocessed, deathrow = collections.deque([kill]), []
        p2c = collections.defaultdict(list)
        for i in range(len(pid)):
            p2c[ppid[i]].append(pid[i])
        while unprocessed:
            deathrow.append(unprocessed.popleft())
            unprocessed.extend(p2c[deathrow[-1]])
        return deathrow
