class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        curMin = prices[0] if prices else 0
        for curPrice in prices[1:]:
            curMin = min(curMin, curPrice)
            maxProfit += curPrice - curMin
            curMin = curPrice
        return maxProfit

    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit
        """
        # sol1: peaks and valleys
        if len(prices) < 2: return 0
        profit = 0
        i = 1
        while i < len(prices):
            while i < len(prices) and prices[i] <= prices[i-1]:
                i += 1
            buy = i-1
            while i < len(prices) - 1 and prices[i+1] >= prices[i]:
                i += 1

            if i < len(prices):
                profit += prices[i] - prices[buy]
                print(prices[buy], prices[i])
            i += 1

        return profit
        """
