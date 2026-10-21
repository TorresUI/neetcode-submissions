class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        if len(s) != len(t):
            return False

        for i in s:
            sMap[i] = 1 + sMap.get(i, 0)
        
        for i in t:
            tMap[i] = 1 + tMap.get(i, 0)

        
        return sMap == tMap
