class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                break
            
        #Now we are at the intersection point where we know there is a cycle
        #Now we must iterate from the beginning until the 2 slow pointers meet
        #and then we found the beginning of the cycle aka the repeated number.
        s2 = 0
        while True:
            s2 = nums[s2]
            s = nums[s]

            if s == s2:
                return s
