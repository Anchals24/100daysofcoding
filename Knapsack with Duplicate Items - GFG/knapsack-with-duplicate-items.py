#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        DP = []
        for row in range(N+1):
            column = [-1] * (W+1)
            DP.append(column)
        
        #initialization
        for i in range(N+1):
            for j in range(W+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
        
        #code
        for i in range(1, N+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    DP[i][j] = max(val[i-1] + DP[i][j-wt[i-1]], DP[i-1][j])
                else:
                    DP[i][j] = DP[i-1][j]
        
        return DP[N][W]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends