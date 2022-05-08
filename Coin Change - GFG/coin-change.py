#User function Template for python3

class Solution:
    def count(self, S, m, n): 
        # code here 
        #Item = S
        #m = arr size
        #n = sum/weight of bag
        DP = []
        for rows in range(m+1):
            column = [-1] * (n+1)
            DP.append(column)
        
        for j in range(n+1):
            DP[0][j] = 0
        for i in range(m+1):
            DP[i][0] = 1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if S[i-1] <= j:
                    DP[i][j] = DP[i][j-S[i-1]]  + DP[i-1][j] 
                else:
                    DP[i][j] = DP[i-1][j] 
        return DP[m][n] 


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends