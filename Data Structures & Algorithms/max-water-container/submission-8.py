class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        #in order to maximize maxArea we want max length and height. lets start at the max height and go inward as we find a larger height.
        res = 0
        while l < r:
            #Calculate the minHeight so we know how tall the container is
            minHeight = min(heights[l], heights[r])

            #Calculate the current length
            length = r - l

            #calculate the area and save against res if its a new max
            res = max(res, minHeight * length)

            #Shift either left or right pointer inward whichever is the smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res