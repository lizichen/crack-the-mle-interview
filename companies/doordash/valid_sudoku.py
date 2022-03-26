"""
https://leetcode.com/problems/valid-sudoku/

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. validate the line
        
        """
        
        for i in range(9):
            col = set()
            row = set()
            sq  = set()
            
            for j in range(9):
                rc = board[i][j]
                cc = board[j][i]
                sc = board[int(i//3*3 + j//3)][int(i%3*3 + j%3)]
                
                if rc != '.':
                    if rc not in row:
                        row.add(rc)
                    else:
                        return False
                
                if cc != '.':
                    if cc not in col:
                        col.add(cc)
                    else:
                        return False
                
                if sc != '.':
                    if sc not in sq:
                        sq.add(sc)
                    else:
                        return False
            
        return True
