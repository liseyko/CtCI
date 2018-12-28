import math


class Solution:
    def climbStairs(self, n):
        cache = [1, 1]
        for _ in range(2, n+1):
            cache.append(cache[-1] + cache[-2])
        return cache[n]

    def climbStairs(self, n):
        sqrt5 = math.sqrt(5)
        fibn = pow((1+sqrt5) / 2, n+1) - pow((1-sqrt5) / 2, n+1)
        return int(fibn // sqrt5)
