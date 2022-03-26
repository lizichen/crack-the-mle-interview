"""
https://leetcode.com/problems/sudoku-solver/

"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == '.':
                        for n in range(1, 10):
                            if valid_try(board, i, j, str(n)):
                                board[i][j] = str(n)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
                    
            return True

        def valid_try(board, i, j, n):    
            for row in range(len(board)):
                if board[row][j] == n:
                    return False

            for col in range(len(board[0])):
                if board[i][col] == n:
                    return False

            row_0 = i//3 
            col_0 = j//3

            row_0 *= 3
            col_0 *= 3

            for r in range(row_0, row_0+3):
                for c in range(col_0, col_0+3):
                    if board[r][c] == n:
                        return False
                    
            return True 
            
        solve(board)
