class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice, maxprofit = float('inf'), 0
        for p in prices:
            if p < minprice:
                minprice = p
            else:
                maxprofit = max(maxprofit, p - minprice)
        return maxprofit

    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0] if prices else 0
        for curPrice in prices[1:]:
            minPrice = min(minPrice, curPrice)
            maxProfit = max(maxProfit, curPrice - minPrice)
        return maxProfit
