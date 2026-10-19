class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Binary search problem where we have to account for rotated array
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            #We need to determine what side of the array we are on. Left sorted portion or right sorted portion. 
            #If we are in the left sorted portion then m > nums[l]
            #If we are in the right sorted portion then m < nums[l]
            # - this is because when we rotate the right sorted side is always less than the left sorted side unless the array is fully sorted in ascending order where nums[m] > nums[l]
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                #We are in the left side of the array

                #Left side: minimum value will be m[l] or right sorted side of the array
                #if we need to look for larger values it will beto the right of m

                if target > nums[m] or target < nums[l]:
                    l = m + 1
                elif target < nums[m]:
                    #we look to the right when the target is greater than m or less than the smallest value in the left sorted portion
                    r = m - 1


            else:
                #We are in the right side of the array
                #Right side. going further right will lead to larger values. Going left will lead to smaller values. Going to the left sorted portion will lead to larger values
                if target < nums[m] or target > nums[r]:
                    #If we reach this conditional we know target is between nums[m] and nums[r] so we search the right side
                    r = m - 1
                elif target > nums[m]:
                    #we need to search to the left
                    #First condition: search left for smaller values.
                    #Second condition: search left for left sorted portion
                    l = m + 1

        return -1
