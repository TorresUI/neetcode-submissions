class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #First we want to find what row is target in

        l, r = 0, len(matrix) - 1
        targetRow = []

        while l <= r:
            m = l + ((r - l) // 2)
            middleRow = matrix[m]
            lowerBound, upperBound = middleRow[0], middleRow[-1]

            #Now we need to check if target is greater than this row and if we need to check higher rows or within the bounds or 
            if target <= upperBound and target >= lowerBound:
                #We found out target row
                targetRow = middleRow
                break
            elif target > upperBound:
                l = m + 1
                print("iamhere")
            else:
                r = m - 1
        
        #Now we have our target row and we need to run binary search on it to find the target
        l, r = 0, len(targetRow) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if target == targetRow[m]:
                return True
            elif target > targetRow[m]:
                l = m + 1
            else:
                r = m - 1
        
        return False