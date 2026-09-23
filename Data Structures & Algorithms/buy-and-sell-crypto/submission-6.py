class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        l, r = 0, 1

        while r < len(prices):
            result = max(result, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        
        return result