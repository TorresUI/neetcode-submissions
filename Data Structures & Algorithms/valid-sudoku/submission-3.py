class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnMap = defaultdict(list)
        gridMap = defaultdict(list)
        for r, row in enumerate(board):
            rowSet = set()
            for c, value in enumerate(row):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in rowSet or board[r][c] in columnMap[c] or board[r][c] in gridMap[((r // 3, c // 3))]:
                    return False

                gridMap[(r // 3, c // 3)].append(board[r][c])
                columnMap[c].append(board[r][c])
                rowSet.add(board[r][c])
        
        return True
            
