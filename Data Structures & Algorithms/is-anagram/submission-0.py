class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for i in s:
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1

        
        for i in t:
            if i in tMap:
                tMap[i] += 1
            else:
                tMap[i] = 1

        return sMap == tMap