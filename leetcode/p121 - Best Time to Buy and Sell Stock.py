class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        minprice = float('inf')
        maxprofit = 0
        for p in prices:
            if p < minprice:
                minprice = p
            elif p - minprice > maxprofit:
                maxprofit = p - minprice

        return maxprofit