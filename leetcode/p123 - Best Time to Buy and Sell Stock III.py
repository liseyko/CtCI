class Solution:
    def maxProfit(self, prices):    
        """
        // f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
        // f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
        //          = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
        // f[0, ii] = 0; 0 times transation makes 0 profit
        // f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
        """
        if len(prices) < 2: return 0
        n = 2 # number of max transation allowed
        maxprofit = 0
        f = [[0 for _ in prices] for _ in range(n)]
        for j in range(n):
            tmpMax = f[j][0] - prices[0];
            for i in range(1, len(prices)):
                f[j][i] = max(f[j][i - 1], prices[i] + tmpMax)
                tmpMax = max(tmpMax, f[j - 1][i] - prices[i])
                maxprofit = max(f[j][i], maxprofit)
        return maxprofit

    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        buyOne = buyTwo = prices[0]
        sellOne = sellTwo = 0
        for p in prices:
            buyOne = min(buyOne, p)
            sellOne = max(sellOne, p - buyOne)
            buyTwo = min(buyTwo, p - sellOne)
            sellTwo = max(sellTwo, p - buyTwo)
            print(buyOne, sellOne, buyTwo, sellTwo)
