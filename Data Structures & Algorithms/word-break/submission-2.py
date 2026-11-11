class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                #check if the sums of the length exceed the total length of the word if yes then just skip
                #Since we are iterating backwards the len - i is the remainder and so the len(w) should be less than or equal to that number
                if i + len(w) > len(s):
                    #Word is too big so just skip
                    continue
                
                #otherwise the word does fit in the spot
                if s[i:len(w) + i] == w:
                    #the beginning of our substring matches the word in the dictionary.
                    #check if this word can be solved with previous solution
                    dp[i] = dp[i + len(w)]
                    if dp[i] == True:
                        break
        return dp[0]