class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxSize = 0

        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            #otherwise we need to process (r, c)
            visited.add((r, c))

            #Need to find the maximum number in all directions and then return the max + 1
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            directionTotal = 0

            for rd, cd in directions:
                directionTotal += bfs(r + rd, c + cd)
            return 1 + directionTotal

        #iterate through the grid.
        #if the current pos we are at is not visited and it is an island. use bfs to mark the whole island as visited and increment island count by one
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxSize = max(maxSize, bfs(r, c))
        
        return maxSize