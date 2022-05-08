#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        #code here
        DP = []
        for rows in range(n+1):
                column = [-1] * (m+1)
                DP.append(column)
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    DP[i][j] = 1 + DP[i-1][j-1]
                else:
                    DP[i][j] = 0
        maxi = -99999999999999999
        for i in range(n+1):
            for j in range(m+1):
                if DP[i][j] > maxi:
                    maxi = DP[i][j]
        return maxi
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends