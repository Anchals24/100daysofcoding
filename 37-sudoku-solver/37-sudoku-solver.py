class Solution:
    
    def issafe(self, row, col, board, value):
        for i in range(9):
            if board[row][i] == value:
                return False
            if board[i][col] == value:
                return False
            if board[3* (row//3) + i// 3][3 * (col//3) + i % 3] == value:
                return False
        return True
        
    def solve(self, board):
        n = 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for k in range(1, 10):
                        if self.issafe(i, j, board, str(k)):
                            board[i][j] = str(k)
                            aagey = self.solve(board)
                            if aagey:
                                print(board)
                                return True
                            else:
                                board[i][j] = "."
                    return False     
        return True
                                
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)