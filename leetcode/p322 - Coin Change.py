class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        maxval = 2147483647
        sol = [0] + [maxval for _ in range(amount)]
        
        for subval in range(1, amount + 1):
            for c in coins:
                if c <= subval:
                    sol[subval] = min(sol[subval], sol[subval - c] + 1)
                #else:
                #    break
        if sol[amount] == maxval:
            return -1
        else:
            return sol[amount]