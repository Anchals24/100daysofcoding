class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = prices[-1]
        diff = 0
        for i in range(len(prices)-2 , -1 , -1):
            if prices[i] > maxi:
                maxi = prices[i]
            else:
                dif = maxi - prices[i]
                diff = max(diff, dif)
        return diff
                
        