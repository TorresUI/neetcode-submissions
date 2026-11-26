class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        tmp = []
        for i in range(len(nums)):
            if nums[i] == val:
                k -= 1
            else:
                tmp.append(nums[i])
        
        for i in range(len(nums)):
            if i in range(len(tmp)):
                nums[i] = tmp[i]

        return k