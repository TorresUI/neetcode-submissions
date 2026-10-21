class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(i, curr):
            if i >= len(nums):
                self.res.append(curr.copy())
                return
            
            #process one branch where we consider i and add it to curr
            curr.append(nums[i])
            dfs(i + 1, curr)

            #process other branch without i
            curr.pop()
            dfs(i + 1, curr)
        
        dfs(0, [])
        return self.res