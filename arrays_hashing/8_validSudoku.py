class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            row_set = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in row_set:
                    return False
                else:
                    row_set.add(board[row][col])

        for col in range(9):
            col_set = set() 
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in col_set:
                    return False
                else:
                    col_set.add(board[row][col])       

        for row in range(0, 9, 3): # [i = 0 ]
            for col in range(0, 9, 3):
                box_set = set()
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        if board[r][c] == ".":
                            continue
                        elif board[r][c] in box_set:
                            return False
                        else:
                            box_set.add(board[r][c])

        return True