class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while l < len(numbers):
            if(r == len(numbers)):
                l += 1
                r = l + 1
            
            numberSum = numbers[l] + numbers[r]
            if numberSum == target and numbers[l] != numbers[r]:
                return [l + 1, r + 1]
            if numberSum > target:
                l += 1
                r = l + 1
            else:
                r += 1
        return false

            