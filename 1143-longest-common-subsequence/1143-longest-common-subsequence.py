class Solution:    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #tabulation/iterative
        n = len(text1)
        m = len(text2)
        DP = []
        for rows in range(n+1):
                column = [-1] *(m+1)
                DP.append(column)
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = max(DP[i][j-1], DP[i-1][j])
        return DP[n][m]
                    
            
        
        
        