class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return 
            
            #process i 
            curr.append(candidates[i])
            total += candidates[i]
            dfs(i+1, curr, total)

            #skip i
            total -= candidates[i]
            curr.pop()
            
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res
    
