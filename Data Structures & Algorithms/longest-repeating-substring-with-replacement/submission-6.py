class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        freqMap = {}
        highestFreq = 0
        longestLength = 0
        while r < len(s):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            highestFreq = max(highestFreq, freqMap[s[r]])

            while (r - l + 1) - highestFreq > k:
                freqMap[s[l]] -= 1
                l += 1
            
            longestLength = max(longestLength, (r - l + 1))
            r += 1
        
        return longestLength
            

