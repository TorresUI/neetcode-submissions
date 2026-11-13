class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #interpreting the problem

        #you are only allowed to move down and right
        #so when you are in the bottom row the only option is to go to the right therefore there is only 1 unique path to get to the prize
        #when you are on the right most column you can only go down so there is only 1 unique path to get to the prize

        #these two serve as the base case for the problem where all other tiles on the grid their unqiue possible combinations are the sum of the possibilities from the right and left.

        #We need to build this solution starting from the bottom right and compute the values until we reach the top left that way we avoid recomputing values if we were to implement this soltuion starting at the top left.

        prevRow = [1] * n

        #set row to be all 1's. This is the bottom row base case. we will start building rows from [1, m]

        #only iterating m-1 times since the bottom row is already built.
        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                #(n-2 that way we never reach the last column which is n -2 as it should stay as 1.)
                #iterate backwards since every value is dependent on the value that comes after and the bottom row
                newRow[j] = newRow[j + 1] + prevRow[j]
            prevRow = newRow
        
        return prevRow[0]
