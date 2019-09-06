class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {n: i for i, n in enumerate(list1)}
        d2 = {n: i for i, n in enumerate(list2)}
        d = collections.defaultdict(list)
        i = float('inf')
        for n in d1.keys() & d2.keys():
            s = d1[n] + d2[n]
            d[s].append(n)
            i = min(i, s)
        return d[i]

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        d1 = {n: i for i, n in enumerate(list1)}
        rd = collections.defaultdict(list)
        ri = float('inf')
        for i, n in enumerate(list2):
            if n in d1:
                idx = i+d1[n]
                rd[idx].append(n)
                ri = min(ri, idx)
        return rd[ri]

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            list1, list2 = list2, list1
        d1 = {n: i for i, n in enumerate(list1)}
        ri, res = 1e9, []
        for i, n in enumerate(list2):
            if n not in d1:
                continue
            idx = i + d1[n]
            if idx > ri:
                continue
            if idx < ri:
                ri, res = idx, []
            res.append(n)
        return res
