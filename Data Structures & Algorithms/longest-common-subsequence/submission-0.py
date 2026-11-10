class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for j in range(len(text1) + 1):
            newRow = []
            for i in range(len(text2) + 1):
                newRow.append(0)
            dp.append(newRow)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]