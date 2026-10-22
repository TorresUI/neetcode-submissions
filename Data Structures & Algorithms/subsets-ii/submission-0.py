class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            #Include ith value
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            #Skip over duplicates
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            #skip i
            i += 1
            dfs(i)
        
        dfs(0)
        return res
