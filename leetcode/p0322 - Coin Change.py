class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [0]+[amount+1]*amount
        for c in coins:
            for i in range(c, len(res)):
                res[i] = min(res[i], res[i-c]+1)
        return res[amount] if res[amount] <= amount else -1

class Solution:
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

