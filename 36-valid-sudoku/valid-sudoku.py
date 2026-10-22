class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for row in range(9):
            row_seen=set()
            for i in range(9):
                if(board[row][i] == "."):
                    continue
                if(board[row][i] in row_seen):
                    return False
                row_seen.add(board[row][i])
        for column in range(9):
            col_seen=set()
            for i in range(9):
                if(board[i][column] == "."):
                    continue
                if(board[i][column] in col_seen):
                    return False
                col_seen.add(board[i][column])
        
        for square in range(9):
            sqr_seen=set()
            for i in range(3):
                for j in range(3):
                    row=(square // 3) * 3 + i
                    col=(square % 3) * 3 + j

                    if(board[row][col] == "."):
                        continue
                    if(board[row][col] in sqr_seen):
                        return False
                    sqr_seen.add(board[row][col])

        return True

                
            
        
                

                
        