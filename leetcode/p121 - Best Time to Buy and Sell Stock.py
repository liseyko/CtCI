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

    def maxProfit(self, prices):
        hi = lo = prices[0] if prices else None
        res = 0
        for p in prices[1:]:
            lo = min(lo, p)
            res = max(res, p - lo)
        return res
