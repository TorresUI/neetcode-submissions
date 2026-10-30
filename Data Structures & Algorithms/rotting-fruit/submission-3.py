class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fruit = 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fruit += 1
                elif grid[r][c] == 2:
                    q.append([r, c])
        
        
        #We now know how many fresh fruit exist and we have a queue full of rotten fruit from which we can BFS from and rot all connected fresh fruit

        while q and fruit > 0:
            for i in range(len(q)):
                #iterate over all items in the queue 
                r, c = q.popleft()
                #(r,c) is a rotten fruit we need to append all of its neighbors
                directions = [[1,0], [-1,0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if newR not in range(rows) or newC not in range(cols) or grid[newR][newC] != 1:
                        continue
                    
                    #otherwise rot it and add it to the queue
                    fruit -= 1
                    grid[newR][newC] = 2
                    q.append([newR, newC])
            time += 1
        #When the queue ends our BFS from all rotten fruit is finished. if there is any remaining fruit then fruit > 0

        return time if fruit == 0 else -1

