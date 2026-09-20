class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for index, num in enumerate(nums):
            numMap[num] = index

        for index, num in enumerate(nums):
            numTarget = target - num
            if numTarget in numMap and index != numMap[numTarget]:
                return [index, numMap[numTarget]]
    
