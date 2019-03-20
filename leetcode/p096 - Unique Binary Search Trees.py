class Solution:
    def _numTrees(self, n: int) -> int:
        if n in self.res:
            return self.res[n]
        numberOfUniqueBST = 0
        for i in range(n):
            numberOfUniqueBST += self._numTrees(i) * self._numTrees(n-1-i)
        self.res[n] = numberOfUniqueBST
        return numberOfUniqueBST

    def numTrees(self, n: int) -> int:
        self.res = {0: 1, 1: 1}
        return self._numTrees(n)
