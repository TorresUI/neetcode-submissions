class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = defaultdict(list)
        for s in strs:
            freqArray = [0] * 26
            for char in s:
                letterIndex = ord(char) - ord('a')
                freqArray[letterIndex] += 1 
            
            resMap[tuple(freqArray)].append(s)
                    
        return list(resMap.values())