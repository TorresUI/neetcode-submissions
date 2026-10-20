class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        #now that we have a sorted array we can do two things.
        #1. for each int in the array we can just do two pointer to find the other 2 
        i = 0
        while i < len(nums):
            #Since we want to avoid duplicates if there are any duplicate numbers they will be next to each other since we ordered the list.
            while i > 0 and i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            
            #This ensures we wont get duplicates

            l, r = i + 1, len(nums) - 1

            #iterate through the subArray excluding i and see if there is any num that results in 0
            while l < r:
                currentSum = nums[l] + nums[r] + nums[i]

                if currentSum == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif currentSum > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
        return res

