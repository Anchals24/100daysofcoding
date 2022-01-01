import copy
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mat = copy.deepcopy(matrix)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    for a in range(len(matrix[i])):
                        matrix[i][a] = 0
                    for b in range(len(matrix)):
                        matrix[b][j] = 0
        #print(matrix)
        
                        
        