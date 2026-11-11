class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        #dp[0] is the base case we need this so that when we are computing a dp value that is the same as a coin it will result in dp[i] = 1 + dp[i - coin]
        #if i and coin are the same it will be 1 + dp[0] so 1 which dp[5] = 1 when there is a 5 coin

        for i in range(1, amount + 1):
            #For each number up until our amount. we want to calculate the minimum amount of coins it takes to build each number. so we have to check what the minimum is for each number
            for c in coins:
                #Check for negative case where c causes dp[negative]
                if i - c < 0:
                    continue
                
                #Check dp[i - c]
                #Compare against current minimum so we can get the minimum across all coins        
                dp[i] = min(dp[i], 1 + dp[i - c])
        return dp[-1] if dp[-1] != (amount + 1) else -1