class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = [1]+[0]*(amount)
        for c in coins:
            for i in range(c, len(res)):
                res[i] += res[i-c]
        return res[amount]
