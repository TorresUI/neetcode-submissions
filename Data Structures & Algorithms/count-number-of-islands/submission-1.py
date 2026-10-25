class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            #We have a position which we know is and island and not visited. we need to recursively check all directions. if it is not in range or if it is visited we terminate
            if r not in range(rows) or c not in range(cols) or (r, c) in visited or grid[r][c] == "0":
                return
            
            #otherwise we found a new tile. add it to visited and seach the rest of the tiles in all 4 directions
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                bfs(r + dr, c + dc)
            
            return

        #iterate through the grid.
        #if the current pos we are at is not visited and it is an island. use bfs to mark the whole island as visited and increment island count by one
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island += 1
        
        return island