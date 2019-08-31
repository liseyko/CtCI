class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k
        same, diff = k, k*(k-1)
        for _ in range(n-2):
            same, diff = diff, (same+diff)*(k-1)
        return same + diff
