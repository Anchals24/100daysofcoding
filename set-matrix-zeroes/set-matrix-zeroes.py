class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [0]*len(matrix) #[0,1,0]
        columns = [0]*len(matrix[0]) #[0,1,0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    columns[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if rows[i] == 1 or columns[j] == 1:
                    matrix[i][j] = 0
        