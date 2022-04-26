class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        D = {}
        for n in nums:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1
        for n in nums:
            if D[n] > majority:
                return n
        