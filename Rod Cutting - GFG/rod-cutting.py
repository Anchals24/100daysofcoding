#User function Template for python3

class Solution:
    def unboundedknap(self, price, length, N, n):
        """
        unbounded knap:
        price = val
        length = weight
        N(length of length/items arr) = N(length of weight/items arr)
        n(max length of rod) = W(max weight of bag)
        """
        DP = []
        for rows in range(N+1):
            column = [-1] * (n+1)
            DP.append(column)
        
        #initialization 
        for i in range(N+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    DP[i][j] = 0
            
        for i in range(1, N+1):
            for j in range(1, n+1):
                if length[i-1] <= j:
                    DP[i][j] = max(price[i-1] + DP[i][j-length[i-1]], DP[i-1][j])
                else:
                    DP[i][j] = DP[i-1][j]
                    
        return DP[N][n]
        
    def cutRod(self, price, n):
        #code here
        length = []
        for i in range(1, n+1):
            length.append(i)
        N = len(length)
        return self.unboundedknap(price, length, N, n)
        
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends