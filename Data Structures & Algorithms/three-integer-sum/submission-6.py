class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, num in enumerate(nums):
            if index > 0 and num == nums[index - 1]:
                continue
            
            l, r = index + 1, len(nums) - 1

            while l < r:
                target = 0 - num
                currentSum = nums[l] + nums[r]

                if currentSum == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                elif currentSum > target:
                    r -= 1
                else:
                    l += 1
            
        return res
                
