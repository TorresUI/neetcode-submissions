class Solution:
    def longestPalindrome(self, s: str) -> str:
        resString = ""

        for i in range(len(s)):
            #Start at the middle
            r, l = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                #Keep exploring and updating resString
                if len(resString) < len(s[l: r + 1]):
                    resString = s[l: r + 1]
                l -= 1
                r += 1
            
            #Now we should have the longest length palindromic substring for an odd length substring.
            #we need to check even length substrings
        
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #Keep exploring and updating resString
                if len(resString) < len(s[l: r + 1]):
                    resString = s[l: r + 1]
                l -= 1
                r += 1
        
        return resString