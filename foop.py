"""
419. Battleships in a Board
Medium

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
"""

# approach: use the fact that since we are traversing the matrix forward; we only have to look behind!!!!! i.e. the cell above and the cell to the left board[r - 1][c] and board[r][c - 1] butttt make sure we are not at the first row or column

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """ 
        traverse the matrix using the fact that if we reached 
        """
        ships = 0
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                
                if r > 0 and board[r - 1][c] == "X":
                    continue
                
                if c > 0 and board[r][c - 1] == "X":
                    continue
                
                ships += 1
                
        return ships