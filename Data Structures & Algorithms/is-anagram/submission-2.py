class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = [0] * 26
        tArray = [0] * 26

        for i in s:
            index = ord(i) - ord('a')
            sArray[index] += 1
        
        for i in t:
            index = ord(i) - ord('a')
            tArray[index] += 1

        return sArray == tArray
