class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(i, curr, total):
            if total == target:
                self.res.append(curr.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            #Process including i 
            total += nums[i]
            curr.append(nums[i])
            dfs(i, curr, total)

            #Process not including i and moving on
            total -= nums[i]
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return self.res
