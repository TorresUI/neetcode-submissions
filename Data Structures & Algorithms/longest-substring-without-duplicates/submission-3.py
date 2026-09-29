class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentSubstring = set()
        res = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in currentSubstring:
                currentSubstring.remove(s[l])
                l += 1
            currentSubstring.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        

        return res