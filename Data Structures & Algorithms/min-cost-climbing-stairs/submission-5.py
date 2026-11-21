class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #costs 0 to go to the top when you are already there
        cost.append(0)
        #min cost at the last step is the last step
        #minCost at the step before is that cost as well we can use these as our base cases
        
        for i in range(len(cost) - 3, -1, -1):
            #the cost at each step is the price of the current + the minimum of either taking 1 or two steps.
            cost[i] = cost[i] + min(cost[i+1], cost[i + 2])

        return min(cost[0], cost[1])