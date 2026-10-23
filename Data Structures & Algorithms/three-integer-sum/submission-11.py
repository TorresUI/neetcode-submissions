class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):

            #skip duplcates for a 

            while i < len(nums) and i > 0 and nums[i] == nums[i - 1]:
                i += 1
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                targetSum = nums[i] + nums[l] + nums[r]

                if targetSum > 0:
                    r -= 1
                elif targetSum < 0:
                    l += 1
                else:
                    #We need to add to the result array
                    res.append([nums[i], nums[l], nums[r]])
                    #We need to skip duplicates in 2nd index
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    r -= 1
            i += 1

        return res