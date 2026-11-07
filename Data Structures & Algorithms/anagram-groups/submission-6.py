class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use an alphabet array as a key 
        alpha = [0] * 26
        groups = defaultdict(list)

        for s in strs:
            currArray = alpha.copy()

            for i in s:
                #iterate through all letters in the string
                currArray[ord('a') - ord(i)] += 1
            
            groups[tuple(currArray)].append(s)
        
        return list(groups.values())