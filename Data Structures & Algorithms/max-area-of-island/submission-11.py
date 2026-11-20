class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxArea = 0
        visited = set()

        #Define a dfs function that returns the max area of an island.
        def dfs(r, c):
            #basecase needs to be if we find a water or an already visited land peice return 0 since it does not add anything to our land area
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            #otherwise we found a piece of land and we need to process it and recursively find its area
            visited.add((r, c))
            area = 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            return area

        for r in range(rows):
            for c in range(cols):
                #find new islands and process their area then take the max.
                if grid[r][c] == 1 and (r, c) not in visited:
                    #new island
                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea