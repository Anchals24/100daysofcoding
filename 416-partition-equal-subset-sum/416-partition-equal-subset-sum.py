class Solution:
    def subsetsum(self, nums, summ, n):
        #To write whether the array contains a subset whose sum is equivalent to the given sum.
        #This is basically a subset sum problem. Will be doing it using recursion + memoization first.
        #This is also a variation of 0-1 knapsack.
        
        #creating a 2D matrix for the changing variables. taking rows as n+1 and columns as summ+1
        DP = []
        for row in range(n+1):
            column = [-1] * (summ+1)
            DP.append(column)
        #initialization
        for j in range(summ+1): 
            DP[0][j] = False
        for i in range(n+1):
            DP[i][0] = True
        #code
        for i in range(1, n+1):
            for j in range(1, summ+1):
                if nums[i-1] <= j:
                    DP[i][j] = DP[i-1][j-nums[i-1]] or DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j]
        return DP[n][summ]
             
    def canPartition(self, nums: List[int]) -> bool:
        summ = 0
        for n in nums:
            summ = summ + n
        if summ % 2 != 0:
            return False 
        return self.subsetsum(nums, summ//2, len(nums))
        
        