class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            #Proccess current
            total += candidates[i]
            currCopy = curr.copy()
            currCopy.append(candidates[i])
            dfs(i + 1, currCopy, total)

            #skip current
            total -= candidates[i]
            currCopy.pop()

            #Skip duplicates
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, currCopy, total)
        dfs(0, [], 0)

        return res