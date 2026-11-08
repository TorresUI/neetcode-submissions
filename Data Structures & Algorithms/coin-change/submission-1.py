class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Amount + 1 is the max number that is unreachable. we will use this as a default value since all real numbers are supposed to be less than this,
        #We initialize to size of amount + 1 because 0 - amount
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for c in coins:
                #We need to subtract each coin 
                if i - c >= 0:
                    #This makes sure the current number we are trying to find the minimum combinations of coin for is greater than the coin number. That way we are not exceeding the total allowed

                    dpValue = i - c
                    dp[i] = min(1 + dp[dpValue], dp[i])
        return dp[amount] if dp[amount] != (amount + 1) else -1
