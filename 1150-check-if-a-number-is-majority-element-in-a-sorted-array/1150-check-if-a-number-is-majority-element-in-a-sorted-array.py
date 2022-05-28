class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        D = {}
        majority = len(nums) // 2
        for n in nums:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1
        if target in D and D[target] > majority:
            return True
        return False
        
        