class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            #Check for any Null operation and skip
            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
                return

            #Otherwise we know that the current (r, c) is an X that is connected to an X on the perimieter of the board
            #Process the current cell and then check all 4 directions
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        #First we want to check the perimeter of the board and find all X's
        for r in range(rows):
            #check column 0 and column cols - 1
            dfs(r, 0)
            dfs(r, cols - 1)
        
        #Check top and bottom rows
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        #Now we iterate through and change all X's to O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        

        