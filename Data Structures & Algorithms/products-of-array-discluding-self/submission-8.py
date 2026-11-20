class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArray = []
        prefixProd = 1
        for i in nums:
            prefixArray.append(prefixProd)
            prefixProd *= i
        
        postfixArray = [0] * len(nums)
        postfixProd = 1

        for i in range(len(nums) - 1, -1, -1):
            postfixArray[i] = postfixProd
            postfixProd *= nums[i]
        
        for i in range(len(nums)):
            nums[i] = postfixArray[i] * prefixArray[i]
        
        return nums