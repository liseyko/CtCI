class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        s1 = collections.defaultdict(int)
        s2 = collections.defaultdict(int)
        for a in A:
            for b in B:
                s1[a+b] += 1
        for c in C:
            for d in D:
                s2[c+d] += 1
        res = 0
        for n in s2.keys():
            res += s2[n] * s1[-n]
        return res

    def fourSumCount(self, A, B, C, D):
        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)
