class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        #find all tresure chests and BFS from them at the same time
        q = collections.deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        #Now we have all the treasure chests in the queue. We need to find all the land tiles and change them to the distance
        distance = 1
        while q:
            for i in range(len(q)):
                #iterate over everything in the queue. initially this is going to be populated with the treasure chests.
                r, c = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if newR not in range(ROWS) or newC not in range(COLS) or grid[newR][newC] != 2147483647:
                        continue
                    
                    #otherwise add it to visited and change it to the current distance
                    print("iamhere", newR, newC)
                    grid[newR][newC] = distance
                    q.append([newR, newC])
            distance += 1
        
