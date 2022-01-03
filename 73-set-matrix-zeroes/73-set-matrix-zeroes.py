class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowl = len(matrix) #3 >> 0,1,2
        coll = len(matrix[0]) #4 >> 0,1,2,3
        """
        [
        [1,1,1,1]  
        [1,0,1,1]  
        [1,1,1,1]
        ]
        """
        row = False
        col = False
        for i in range(rowl): #i=1
            if matrix[i][0] == 0:
                col = True
            for j in range(coll): #j = 1
                if i == 0:
                    if matrix[0][j] == 0:
                        row = True
                if i != 0 and j != 0:
                    if matrix[i][j] == 0:
                        matrix[i][0] = 0 
                        matrix[0][j] = 0
        for i in range(1, rowl):
            for j in range(1, coll):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row == True:
            for j in range(coll):
                matrix[0][j] = 0
        if col == True:
            for i in range(rowl):
                matrix[i][0] = 0
        
            
            
                    
            