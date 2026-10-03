class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m

            #Are we in the left sorted portion?

            if nums[l] <= nums[m]:
                #We are in the left sorted portion. 
                #regular binary search

                if target > nums[m]:
                    #we know the left only decreases so check right
                    l = m + 1
                elif target < nums[m]:
                    if target < nums[l]:
                        #right side has smaller values:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    if target > nums[r]:
                        r = m - 1
                    else:
                        l = m + 1
        return -1


