class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #Do a dfs from each rotten fruit and then rot all fruit. at each level increment the number of minutes.
        #if at the end the number of rotted fruit does not equal the number of fruit there were at the beginning then return -1 

        #first we want to initialize the q with the rotten fruit and get a count for total amount of fresh fruit
        fresh = 0
        q = collections.deque()
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        #now we have a count of fresh fruit as well as initialized the q with rotten fruit.
        minutes = 0

        while q and fresh > 0:
            print(q, minutes)

            for i in range(len(q)):
                currentR, currentC = q.popleft()

                #rot the fruit and explore its neighbors. This will be for all fresh fruit in the q after the initial exploration from the rotten q                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    newR, newC = currentR + dr, currentC + dc
                    if newR in range(rows) and newC in range(cols) and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        fresh -= 1
                        q.append([newR, newC])
                
            minutes += 1
        return minutes if fresh == 0 else -1
                

