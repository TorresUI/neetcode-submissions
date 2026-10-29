class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        mostFreq = 0
        freqMap = {}
        res = 0
        while r < len(s):
            #First we need to process R and add it to the string
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            mostFreq = max(mostFreq, freqMap[s[r]])

            while (r - l + 1) - mostFreq > k:
                freqMap[s[l]] -= 1
                l += 1
                
            
            newLength = r - l + 1
            res = max(res, newLength)

            r += 1
        return res
