class Solution:
    def isArmstrong(self, N: int) -> bool:
        ml, t = [], N
        while t:
            ml.append(t % 10)
            t //= 10
        k = len(ml)
        while ml:
            t += ml.pop() ** k
        return t == N

    def isArmstrong(self, n: int) -> bool:
        ns = str(n)
        return sum(int(x) ** len(ns) for x in ns) == n
