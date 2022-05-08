#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
		# code here
		#DP = [[-1] * (sum+1) for row in range(n+1)]
		DP = []
		for row in range(n+1):
		    column = []
		    for c in range(sum+1):
		        column.append(-1)
		    DP.append(column)
		    
	    for j in range(sum+1): 
            DP[0][j] = 0
        DP[0][0] = 1
	    for i in range(1, n+1):
	        for j in range(0, sum+1):
	           if arr[i-1] > j:
	               DP[i][j] = DP[i-1][j]
	           else:
	               DP[i][j] = DP[i-1][j-arr[i-1]] + DP[i-1][j]
	    ans = DP[n][sum]
	    return ans % 1000000007
	    
	    """
	    DP = []
        for row in range(n+1):
        for columns in range(sum+1):
        column = [-1] * (sum+1) #[-1, -1, -1, -1, -1, -1]
        DP.append(column)
	    """
	                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends