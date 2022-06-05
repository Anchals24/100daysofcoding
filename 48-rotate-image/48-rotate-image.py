class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])
        for r in range(row):
            for c in range(r, column):
                matrix[r][c] , matrix[c][r] = matrix[c][r], matrix[r][c]
        for m in matrix:
            m.reverse()
            