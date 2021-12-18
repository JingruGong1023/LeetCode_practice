class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        profit =0
        minPrice = prices[0]
        for i in range(1,len(prices)):
            
            profit = max(profit, prices[i]-minPrice)
            minPrice = min(minPrice, prices[i])
            
        return profit
      
      #O(n)
