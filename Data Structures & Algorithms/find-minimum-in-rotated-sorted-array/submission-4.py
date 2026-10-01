class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 999
        while l <= r: 
            m = l + ((r - l) // 2)

            if nums[m] >= nums[l]:
                #we must be in the left side of the array sorted from l -> m
                if nums[l] > nums[r]:
                    #we need to search in the right side
                    l = m + 1
                else:
                    res = min(res, nums[m])
                    r = m - 1

            else:
                #we must be in the right side of the array sorted from m -> r
                res = min(res, nums[m])
                r = m - 1
        return res
