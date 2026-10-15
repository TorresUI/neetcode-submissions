class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #We need to iterate through the board for all columns and rows.

        #at each row we need to check that there are no duplicates
        #At each column
        subboxMap = defaultdict(set)
        columnMap = defaultdict(set)

        for r in range(len(board)):
            row = board[r]
            rowSet = set()
            for c in range(len(row)):

                if board[r][c] == '.':
                    continue
                
                #otherwise we have encountered a number for [r][c]
                #Check if it is already in the row
                #Check if it is already in the column
                #Check if it is already in the sub-box
                if board[r][c] in rowSet:
                    return False
                
                if c in columnMap and board[r][c] in columnMap[c]:
                    return False
                
                subRow, subColumn = r // 3, c // 3

                if subboxMap[(subRow, subColumn)] and board[r][c] in subboxMap[(subRow, subColumn)]:
                    return False
                
                rowSet.add(board[r][c])
                columnMap[c].add(board[r][c])
                subboxMap[(subRow, subColumn)].add(board[r][c])
            
        return True

                


                
                

                