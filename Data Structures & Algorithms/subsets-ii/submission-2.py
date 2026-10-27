class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        def backtracking(i):
            if i >= len(nums):
                #we have reached the end of the word. append a copy of the word
                res.append(curr.copy())
                return
            
            #We need to take 2 steps. 1 process the current letter and move to the next one 

            #2 skip the current letter and skip all duplicates after the first duplicate [1, 1] is processed.

            #step1:
            curr.append(nums[i])
            backtracking(i + 1)

            #step2:
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                print(i)
                i += 1
            backtracking(i + 1)

        backtracking(0)
        return res