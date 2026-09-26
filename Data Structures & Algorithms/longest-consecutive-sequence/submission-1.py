class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for i in nums:
            consecutiveCount = 1
            if i - 1 not in numSet:
                c = 1
                while (i + c) in numSet:
                    c += 1
                res = max(res, c)
        return res