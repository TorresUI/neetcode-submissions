class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        res = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in substring:
                while s[r] in substring:
                    substring.remove(s[l])
                    l += 1
            substring.add(s[r])
            res = max(res, len(substring))
            r += 1
        
        return res

