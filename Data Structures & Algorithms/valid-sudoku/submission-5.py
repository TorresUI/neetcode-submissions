class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        sectionMap = defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                #define section
                sectionR = r // 3
                sectionC = c // 3
                #process row.
                if (board[r][c] in rowMap[r]) or (board[r][c] in colMap[c]) or (board[r][c] in sectionMap[(sectionR, sectionC)]):
                    return False
                
                #otherwise we have a new number lets process it
                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                sectionMap[(sectionR, sectionC)].add(board[r][c])
        
        return True


                