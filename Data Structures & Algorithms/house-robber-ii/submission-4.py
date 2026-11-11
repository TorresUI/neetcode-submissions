class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robStreet(nums):
            nums.append(0)
            for i in range(len(nums) - 3, -1, -1):
                nums[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            return nums[0]

        if len(nums) == 1:
            return nums[0]

        street1 = robStreet(nums[1:])
        street2 = robStreet(nums[:len(nums) - 1])
        return max(street1, street2)