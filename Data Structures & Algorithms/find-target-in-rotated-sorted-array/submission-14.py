class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            #We need to check if m is located in the left sorted portion or the right sorted portion

            #if nums[0] is less than nums[m] we are in the left sorted portion

            if nums[0] <= nums[m]:
                #left sorted portion 

                #When we are in the left sorted portion smaller numbers are to the left. Smaller numbers can also be to the right in the beginning of the right sorted portion. if the number we are looking for is smaller than [0] then check the right
                #greater numbers are to the right
                if target == nums[m]:
                    return m

                elif target < nums[0] or target >= nums[m]:
                    #target is greater than m so we need to check right
                    #target is less than the lowest value in the LSP so check right               
                    l = m + 1
                
                elif target < nums[m]:
                    #less than m but greater than or equal to nums[0] check left
                    r = m - 1

            
            else:
                #right sorted portion

                if target == nums[m]:
                    return m

                #anything to the left is smaller
                #anything to the right is bigger
                #there could be larger values in the left sorted portion of the array. it depends on if target is > [-1]
                elif target > nums[-1] or target <= nums[m]:
                    #We want to check the left side
                    r = m - 1
                
                elif target > nums[m]:
                    #we know target is > m but less than or equal to nums[-1] so we want to check the right
                    l = m + 1
        return -1