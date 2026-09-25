class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for n in range(len(nums)):
            result[n] = prefix
            prefix *= nums[n]

        postfix = 1

        for n in range(len(nums) - 1, -1, -1):
            result[n] *= postfix
            postfix *= nums[n]
        return result