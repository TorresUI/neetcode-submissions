class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        currentListOfCharacters = set()
        stringLength = 0
        while l < len(s) and r < len(s):
            if s[r] in currentListOfCharacters:
                currentListOfCharacters.remove(s[l])
                l += 1
            else:
                currentListOfCharacters.add(s[r])
                stringLength = max(stringLength, len(currentListOfCharacters))
                r += 1
        
        return stringLength