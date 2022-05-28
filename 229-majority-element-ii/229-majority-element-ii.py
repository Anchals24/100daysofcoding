class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majority = n//3
        D = {}
        for n in nums:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1
        s = set()
        for n in nums:
            if D[n] > majority:
                s.add(n)
        return s
                
        