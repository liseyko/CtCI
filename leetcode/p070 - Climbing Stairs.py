import math

class Solution:
    def __init__(self):
        self.cache = [0,1,2]
        self.sqrt5 = math.sqrt(5)
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < len(self.cache):
            return self.cache[n]
        
        for _ in range(n - len(self.cache) + 1):
            self.cache.append(  self.cache[-1] + self.cache[-2] )
        
        return self.cache[n]


    def climbStairs(self, n):
        fibn = pow((1 + self.sqrt5) / 2, n+1) - pow((1 - self.sqrt5) / 2, n+1);
        return int(fibn // self.sqrt5)
