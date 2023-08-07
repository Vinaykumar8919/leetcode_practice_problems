class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                max_profit = max(maxProfit, prices[i] - prices[buy])
        return maxProfit

        
