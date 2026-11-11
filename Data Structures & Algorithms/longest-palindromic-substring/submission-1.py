class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            #For each char go out both ways and check if its a palindrome

            j, k = i, i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if len(s[j:k+1]) > len(res):
                    res = s[j:k+1]
                
                j -= 1
                k += 1
            
            #We need to check the middle two soltuion as well incase the longest substring is even numbered 
            j,k = i, i + 1

            while j >= 0 and k < len(s) and s[j] == s[k]:
                if len(s[j:k+1]) > len(res):
                    res = s[j:k+1]
                
                j -= 1
                k += 1
        
        return res
