class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(i, currentSum, combo):
            if currentSum == target:
                res.append(combo)
                return
            
            if currentSum > target or i >= len(candidates):
                return
            
            #otherwise at each step we can choose to either take the current number or not
            #take the number
            arrayIncluding = combo.copy()
            arrayIncluding.append(candidates[i])
            backtracking(i + 1, currentSum + candidates[i], arrayIncluding)

            #otherwise dont take
            copyArray = combo.copy()
            newIndex = i + 1
            while newIndex < len(candidates) and candidates[newIndex] == candidates[newIndex - 1]:
                newIndex += 1

            backtracking(newIndex, currentSum, copyArray)
        
        backtracking(0, 0, [])
        return res
