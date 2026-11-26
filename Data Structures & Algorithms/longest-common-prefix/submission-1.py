class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            currentPrefix = strs[0][:i + 1]

            for s in strs:
                if s[:i + 1] != currentPrefix:
                    return res
            
            res = currentPrefix
        return res
                    
            
