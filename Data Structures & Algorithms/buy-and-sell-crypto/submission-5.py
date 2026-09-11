class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprofit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            maxprofit = max(profit, maxprofit)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxprofit    