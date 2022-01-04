class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -1000000000000000000
        add = 0
        for n in nums:
            add = add + n #1
            ans = max(add,ans) #1
            if add < 0:
                add = 0 
        return ans
            
            
            
        