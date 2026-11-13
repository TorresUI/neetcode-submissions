class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Creating subsequences for each string comes with two choices you either take the current letter or you dont.
        #When creating subsequences for both strings you end up with 3 different sub problems.
        #1. both indicies match and you add that to the subsequence. then you shift i for both strings.
        #2. they dont match and you skip one char from string1
        #3. they dont match and yous skip one char from string2

        #so its either 1 or 2&3. The max of 2&3 is the longest common subsequence at that step

        #create a 2d array to represent the longest common subsequence at each combination of substrings initialize out of bounds case as 0 and do a bottom up approach of computing the longest common subsequence at every step until you get to 0,0 then return the result

        dp = []
        #have rows = len(text1) cols = len(text2)
        for r in range(len(text1) + 1):
            row = []
            for c in range(len(text2) + 1):
                row.append(0)
            dp.append(row)
        
        #now that we have the array built we need to build it from bottom up to 0,0 
        #if the chars match then LCS is 1 + LCS(substrings)
        #if they dont match then LCS is the max of i + 1 and j + 1

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    #chars match. 
                    #i + 1 & j + 1 because we are incrementing the pointers down one more to look at the sub problem of the remainder.
                    #in the case of the last matching char. the remainder will be 0 so 1 + 0 is 1.
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    #if they dont match we take the max of the left and bottom values which is iterating one char for the strings. so first 1 char s1 and 1 char s2.
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]