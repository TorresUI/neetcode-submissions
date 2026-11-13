class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])


        def dfs(i, r, c, visited):
            if i >= len(word):
                #We have successfully found all letters in the word so return true
                return True
            
            if r not in range(rows) or c not in range(cols) or board[r][c] != word[i] or (r, c) in visited:
                return False

            #Otherwise we found a word process it and increment i 
            newVisited = visited.copy()
            newVisited.add((r, c))
            i += 1

            #explore all 4 directions
            return dfs(i, r + 1, c, newVisited) or dfs(i, r - 1, c, newVisited) or dfs(i, r, c + 1, newVisited) or dfs(i, r, c - 1, newVisited)
            

        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c, set()):
                    return True
        
        return False