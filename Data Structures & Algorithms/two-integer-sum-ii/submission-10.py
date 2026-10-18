class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            pointerSum = numbers[l] + numbers[r]
            if pointerSum == target:
                return [l + 1, r + 1]
            elif pointerSum > target:
                r -= 1
            else:
                l += 1
        
        