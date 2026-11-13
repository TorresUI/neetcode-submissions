class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Identify all chests.
        #BFS from all of them at the same time and change the cells to be the distance or the level of BFS depth that we are currently at. 

        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        #Now the q is populated with all of the treasure chests
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                #Check if r and c are in bounds. Check to make sure its not a water cell or already visited

                if r not in range(rows) or c not in range(cols) or grid[r][c] == -1 or (r, c) in visited:
                    #Just dont do anything
                    continue
                
                #Otherwise we have a valid space that we need to process
                grid[r][c] = dist
                visited.add((r, c))

                #Add all neighbors for next iteration
                q.append((r + 1, c))
                q.append((r - 1, c))
                q.append((r, c + 1))
                q.append((r, c - 1))
            
            dist += 1
        
        