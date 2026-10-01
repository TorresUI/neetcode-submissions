class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = []
        while l <= r:
            m = l + ((r - l) // 2)

            row = matrix[m]

            if target < row[0]:
                #Target is less than the first row.
                r = m - 1
            elif target > row[0] and target > row[-1]:
                l = m + 1
            elif target >= row[0] and target <= row[-1]:
                #we found the row 
                break

        #Now we can do binary search on the row

        l, r = 0, len(row) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if row[m] == target:
                return True
            elif row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
        
        return False

