class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 1, len(nums) - 2

        prefixArray, postfixArray = [0] * len(nums), [0] * len(nums)
        prefixArray[0] = 1
        postfixArray[-1] = 1
        while l < len(nums):
            prefixArray[l] = nums[l - 1] * prefixArray[l - 1]
            l += 1
        
        while r >= 0:
            postfixArray[r] = nums[r + 1] * postfixArray[r + 1]
            r -= 1
        
        res = []
        for index in range(len(nums)):
            res.append(prefixArray[index] * postfixArray[index])
        
        return res
