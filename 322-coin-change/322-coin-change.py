import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        DP = []
        for row in range(n+1):
            columns = [-1] * (amount+1)
            DP.append(columns)
        #initialization
        for j in range(amount+1):
            DP[0][j] = sys.maxsize - 1
        for i in range(1, n+1):
            DP[i][0] = 0
        for i in range(1, n+1):
            for j in range(1, amount +1):
                if i == 1:
                    if (j % coins[i-1]) == 0:
                        DP[i][j] = (j // coins[i-1])
                    else:
                        DP[i][j] = sys.maxsize - 1           
        #code
        for i in range(2, n+1):
            for j in range(1, amount+1):
                if coins[i-1] > j:
                    DP[i][j] = DP[i-1][j]
                else:
                    DP[i][j] = min(1 + DP[i][j-coins[i-1]], DP[i-1][j])
        if DP[n][amount] != sys.maxsize-1:
            return DP[n][amount]
        return -1
            
        