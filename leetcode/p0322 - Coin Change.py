class Solution(object):
    def coinChange(self, coins: List[int], amount: int) -> int:

        def _coinChange(amount):
            for coin in coins:
                if coin > amount:
                    continue
                res[amount] = min(res[amount], res[amount-coin] + 1)

        maxval = amount + 1
        res = [0] + [maxval] * amount
        for val in range(1, amount+1):
            _coinChange(val)

        return res[amount] if res[amount] < maxval else -1

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
