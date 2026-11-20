class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #iterate through the islands and do a DFS when seeing a new island
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            #because we will recursively call this function check if r, c is a valid new island cell
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == '0':
                return
            
            #we know that we are at an island block that has not been visited.
            #process it and then check all of its neighbors
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    #We found a new island, lets explore the whole thing
                    dfs(r, c)
                    islands += 1
        
        return islands

