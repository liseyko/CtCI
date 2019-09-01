class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n < 2:
            return n*k
        same, diff = k, k*(k-1)
        for _ in range(n-2):
            same, diff = diff, (same+diff)*(k-1)
        return same + diff
