class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = f = 0

        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        s2 = 0
        while s2 != s:
            s2 = nums[s2]
            s = nums[s]
        
        return s2
        