class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n

        for i in range(m - 1):
            #This is the number of rows we need to construct
            currRow = [1] * n
            for j in range(n - 2, -1, -1):
                #We are iterating backwards skipping the rightmost column since that is always [1] given we can only move down
                #Here we are summing the values from the cell to the right and the cell below 
                currRow[j] = currRow[j + 1] + prevRow[j]
            #make currRow the new prevRow for the next iteration
            prevRow = currRow
        
        return prevRow[0]
