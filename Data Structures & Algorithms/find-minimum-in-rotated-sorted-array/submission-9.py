class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            m = l + ((r - l) // 2)
            res = min(res, nums[m])

            #are we in left sorted portion or right?
            if nums[m] >= nums[l]:
                #We are in left sorted portion

                #Where are the min values?
                #If the array is sorted in ascending order and there is only a left sorted portion then the min value is at nums[l]

                if nums[l] > nums[r]:
                    l = m + 1
                else:
                    r = m - 1



                #If the array is rotated then the number at nums[r] will be less than nums[l] therefore the min number will be somewhere between nums[m] and nums[r]        

            else:
                #We are in right sorted portion
                r = m - 1
        return res