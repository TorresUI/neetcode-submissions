class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        return len(nums) != len(numset)