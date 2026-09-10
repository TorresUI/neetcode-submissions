class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            numberSum = numbers[l] + numbers[r]
            if numberSum == target:
                return [l + 1, r + 1]
            if numberSum > target:
                r -= 1
            if numberSum < target:
                l += 1
