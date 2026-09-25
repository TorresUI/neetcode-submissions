class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -99
        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            length = r - l
            res = max(res, height * length)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res