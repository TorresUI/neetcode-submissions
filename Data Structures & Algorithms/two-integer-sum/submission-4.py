class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            numMap[num] = i
        
        for i, num in enumerate(nums):
            if target - num in numMap and i != numMap[target - num]:
                return [i, numMap[target - num]]



        
