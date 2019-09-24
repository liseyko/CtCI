class Solution:

    def __init__(self, weights: List[int]):
        self.maxWeight = 0
        self.idxs = []
        for w in weights:
            self.maxWeight += w
            self.idxs.append(self.maxWeight)

    def pickIndex(self) -> int:
        w = random.randint(0, self.maxWeight-1)
        idx = bisect.bisect(self.idxs, w)
        return idx

    def pickIndex(self) -> int:
        w = random.randint(0, self.maxWeight-1)
        li, ri = 0, len(self.idxs)-1
        while li < ri:
            mi = li + (ri-li) // 2
            if w <= self.idxs[mi]-1:
                ri = mi
            else:
                li = mi+1
        return li
