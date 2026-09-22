class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            res = max(res, length * height)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return res