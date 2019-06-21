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

        if sol[amount] == maxval:
            return -1
        else:
            return sol[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0] + [amount+1]*amount

        for i in range(1, len(res)):
            for c in coins:
                if c <= i:
                    res[i] = min(res[i], res[i-c]+1)

        return res[amount] if res[amount] <= amount else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        res_amt = {}
        for c in coins:
            res_amt[c] = 1

        def change(n: int) -> int:
            if n not in res_amt:
                res_amt[n] = amount+1
                for c in coins:
                    if n > c:
                        res_amt[n] = min(res_amt[n], change(n-c)+1)
            return res_amt[n]
        result = change(amount) if amount else 0
        return result if result <= amount else -1
