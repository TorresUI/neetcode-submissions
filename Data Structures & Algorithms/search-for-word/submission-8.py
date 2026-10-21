class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        

        def backtrackDFS(r, c, index, path):
            if index == len(word):
                return True

            if (r >= rows or r < 0) or (c >= cols or c < 0) or ((r, c) in path) or (board[r][c] != word[index]):
                return False
            
            #otherwise we need to move onto the next letter since we know that the current letter is true and we still have more to go in the word.
            #first add the current spot to the set
            pathCopy = path.copy()
            pathCopy.add((r,c))


            return backtrackDFS(r + 1, c, index + 1, pathCopy) or backtrackDFS(r - 1, c, index + 1, pathCopy) or backtrackDFS(r, c + 1, index + 1, pathCopy) or backtrackDFS(r, c - 1, index + 1, pathCopy)
        
        #We want to run this dfs for all starting points in the grid.

        for r in range(rows):
            for c in range(cols):
                if backtrackDFS(r, c, 0, set()):
                    #if this returns true we found a valid path
                    return True
        
        #If none return true there is no valid path
        return False
            