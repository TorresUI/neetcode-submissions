class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()

        #First lets check the top row (row 0) and bottom row(row - 1) and run dfs on all cells passing in the pac/atl set

        def dfs(r, c, visit, prev):
            #(r,c) is the position
            # visit is the set for the ocean
            # prev is the previous height

            if r not in range(rows) or c not in range(cols) or (r, c) in visit or heights[r][c] < prev:
                #we are doing < prev because we are inverting the rule since we are traversing from the ocean out
                return
            
            #otherwise process the current cell
            visit.add((r, c))
            #dfs on all its neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(cols):
            #First row = pacific
            #Previous height just use itself since we are coming from the ocean there is no previous height and equal height is enough to pass the requirement
            dfs(0, c, pac, heights[0][c])

            #Last row = atl
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        #Do the same for the columns.
        for r in range(rows):
            #First column is pac
            dfs(r, 0, pac, heights[r][0])

            #Second column is atl
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        #Now we should have two populated sets with all cells that reach the respective oceans
        #iterate through the grid and add all cells in both sets to a result list
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res