class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #first I want to find the row that it is in.
        l, r = 0, len(matrix) - 1
        midRow = []
        while l <= r:
            m = l + ((r - l) // 2)

            middleRow = matrix[m]
            
            #We want to check if target is in this row

            if target >= middleRow[0] and target <= middleRow[-1]:
                #we are in the middle row
                midRow = middleRow
                break

            elif target < middleRow[0]:
                r = m - 1
            elif target > middleRow[-1]:
                l = m + 1

        
        l, r = 0, len(midRow) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target == midRow[m]:
                return True
            elif target > midRow[m]:
                l = m + 1
            elif target < midRow[m]:
                r = m - 1
        return False
        
