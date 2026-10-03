class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 9999999999999999999

        while l <= r:
            m = l + ((r - l) // 2)

            res = min(res, nums[m])

            #are we in the left side or right side of the sorted array.

            if nums[m] >= nums[l]:
                #we are in the left side
                if nums[l] < nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #we are in the right side
                r = m - 1

        return res
