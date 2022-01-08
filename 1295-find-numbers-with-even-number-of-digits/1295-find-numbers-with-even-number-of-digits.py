class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            dig = 0
            while n != 0:
                dig += 1
                n = n // 10
            if dig % 2 == 0:
                ans += 1
        return ans
            
        