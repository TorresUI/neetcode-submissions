class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefixArr = []
        for i in nums:
            prefixArr.append(prefix)
            prefix *= i
        

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            #multiply the 
            prefixArr[i] = prefixArr[i] * postfix
            postfix *= nums[i]
        
        return prefixArr
