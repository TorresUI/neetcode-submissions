class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            currentProfit = prices[r] - prices[l]
            profit = max(profit, currentProfit)

            if prices[r] < prices[l]:
                l = r
                r += 1
            else:
                r += 1
        
        return profit