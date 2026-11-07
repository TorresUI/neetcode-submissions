class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #so we know that the price to go from nth step and n-1th step to the top is equal to whatever the price is currently
        #we want to work backwards with these two as our base case and populate the total amount of cost to get from each starting point to the end
        
        for i in range(len(cost) - 3, -1, -1):
            minCost = min(cost[i + 1], cost[i + 2])
            cost[i] += minCost
        
        return min(cost[0], cost[1])
            