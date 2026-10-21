class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        used = [False] * len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                self.res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                #Choose nums[i] as the next element
                used[i] = True
                curr.append(nums[i])
                dfs(curr)

                #Undo the choice
                curr.pop()
                used[i] = False

        dfs([])
        return self.res