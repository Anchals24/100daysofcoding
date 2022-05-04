#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        #taking a matrix of W+1 columns and n+1 rows.
        DP = []
        for row in range(n+1):
            for column in range(W+1):
                columns = [-1] * (W+1)
                DP.append(columns)
                
        #Initialization(equivalent to the recursive code )
        for i in range(n+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
        #filling the remaining ones.
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    DP[i][j] = max(val[i-1]+DP[i-1][j-wt[i-1]], DP[i-1][j])
                else:
                    DP[i][j] = DP[i-1][j]
        return DP[n][W]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends