class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, path):
            if i == len(word):
                return True

            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            newPath = path.copy()
            newPath.add((r, c))   
            return (dfs(r + 1, c, i + 1, newPath) or
                    dfs(r - 1, c, i + 1, newPath) or
                    dfs(r, c + 1, i + 1, newPath) or
                    dfs(r, c - 1, i + 1, newPath))

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0, set()):
                    return True
        return False