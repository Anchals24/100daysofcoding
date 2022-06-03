class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) #3
        col = len(matrix[0])-1 #3
        r = 0
        while (r < row and col >= 0): 
            if matrix[r][col] == target:
                return True
            elif matrix[r][col] > target: #m[1][3]
                col -= 1 #1
            elif matrix[r][col] < target: #mat[0][3] < 
                r += 1 #1
        return False
            
            
            
            
        
        