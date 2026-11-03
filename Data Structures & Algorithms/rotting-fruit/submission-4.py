class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fruit = 0 
        q = collections.deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0

        #first we need to initialize the q as well as get a count for total of fresh fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fruit += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        while q and fruit > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = dr + r, dc + c
                    if newR not in range(rows) or newC not in range(cols) or grid[newR][newC] != 1:
                        continue
                    
                    #otherwise we know that grid[r][c] == 1
                    q.append([newR, newC])
                    grid[newR][newC] = 2
                    fruit -= 1
            time += 1
        
        return time if fruit == 0 else -1

