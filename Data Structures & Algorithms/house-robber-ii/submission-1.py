class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def houseRobber(nums2):
            if len(nums2) == 1:
                return nums2[0]
            nums2[1] = max(nums2[0], nums2[1])
            for i in range(2, len(nums2)):
                nums2[i] = max(nums2[i - 1], nums2[i - 2] + nums2[i])
            return nums2[-1]
            
        if len(nums) == 1:
            return nums[0]
        return max(houseRobber(nums[:len(nums) - 1]), houseRobber(nums[1:]))