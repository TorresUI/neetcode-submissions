class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Want to run dfs at every starting point in the rows/columns
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, visited, i):
            if i == len(word):
                return True
            
            #Otherwise we have to check all conditions that would return a false
            if (r >= rows or r < 0) or (r < 0) or (c >= cols) or (c < 0) or board[r][c] != word[i] or (r, c) in visited:
                return False
            
            #Process letter and move on
            setCopy = visited.copy()
            setCopy.add((r, c))
            i += 1

            #Check in every direction
            return backtrack(r + 1, c, setCopy, i) or backtrack(r - 1, c, setCopy, i) or backtrack(r, c + 1, setCopy, i) or backtrack(r, c - 1, setCopy, i)

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, set(), 0):
                    return True
        return False
