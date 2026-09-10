class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            print([heights[l], heights[r]])
            smallestCurrentBar = min(heights[l], heights[r])
            base = r - l
            maxArea = max(smallestCurrentBar * base, maxArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea