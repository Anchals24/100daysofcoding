class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for n in range(len(nums)):
            subb = target - nums[n]
            if subb in D:
                return [n , D[subb]]
            D[nums[n]] = n
        
                
        