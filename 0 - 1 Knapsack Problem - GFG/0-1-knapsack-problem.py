#User function Template for python3

class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    #Let's try to optimize it using memoization.
    
    def helper(self, W, wt, val, n, DP):
        if n == 0 or W == 0:
            return 0
        if DP[n][W] != -1:
            return DP[n][W]
        if wt[n-1] <= W:
            DP[n][W] = max(val[n-1]+ self.helper(W-wt[n-1], wt, val, n-1,DP), self.helper(W,wt,val,n-1,DP))
            return DP[n][W]
        elif wt[n-1] > W:
            DP[n][W] = self.helper(W,wt,val,n-1,DP)
            return DP[n][W]
            
        
        
        
    def knapSack(self,W, wt, val, n):
        # code here
        #In prev recursive code, we noticed W and n were changing. 
        #Let's take a matrix for the same. 
        #taking n+1 rows and W+1 columns to prevent calling the recursive function over and over again.
        
        DP = []
        for row in range(n+1):
            for column in range(W+1):
                columns = [-1] * (W+1)
                DP.append(columns)
        
        return self.helper(W, wt, val, n, DP)

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