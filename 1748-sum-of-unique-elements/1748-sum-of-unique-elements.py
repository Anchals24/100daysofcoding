class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        D = {}
        for n in nums:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1
        ans = 0
        for n in nums:
            if D[n] == 1:
                ans += n
        return ans
        