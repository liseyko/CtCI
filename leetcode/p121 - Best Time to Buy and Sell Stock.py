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
