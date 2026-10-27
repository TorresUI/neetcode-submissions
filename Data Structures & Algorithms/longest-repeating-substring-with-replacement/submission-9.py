class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        charFreq = {}
        mostFreqChar = 0
        res = 0

        while r < len(s):
            #insert r in charfreq
            charFreq[s[r]] = 1 + charFreq.get(s[r], 0)
            #calculate most frequent char
            mostFreqChar = max(mostFreqChar, charFreq[s[r]])                  
            #We must check if the substring is valid before saving max length of substring
            while (r - l + 1) - mostFreqChar > k:
                #We need to decrease the last character and move l pointer up
                #We need to change mostFreqChar
                charFreq[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
            r += 1
        return res

