class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1] , [1,1]]
        Ans = [[1] , [1,1]] #2
        n = numRows - 2
        for i in range(n):
            Ans2 = [1]
            for j in range(len(Ans[-1])):
                if j < (len(Ans[-1])-1):
                    s = Ans[-1][j] + Ans[-1][j+1]
                    Ans2.append(s)
            Ans2.append(1)
            Ans.append(Ans2)
        return Ans
        
                
                
                
        