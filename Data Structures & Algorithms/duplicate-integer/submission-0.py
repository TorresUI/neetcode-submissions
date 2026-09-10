class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))
        return len(set(nums)) != len(nums)