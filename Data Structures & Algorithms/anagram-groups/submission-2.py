class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            sArray = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                sArray[index] += 1
            if tuple(sArray) in anagramMap:
                anagramMap[tuple(sArray)].append(s)
            else:
                anagramMap[tuple(sArray)] = [s]
        
        return list(anagramMap.values())