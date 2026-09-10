class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middleNum = l + ((r - l) // 2)
            if target > nums[middleNum]:
                l = middleNum + 1

            elif target < nums[middleNum]:
                r = middleNum - 1
                continue

            else:
                return middleNum

        return -1