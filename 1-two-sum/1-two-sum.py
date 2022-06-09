class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        D[nums[0]] = 0
        for n in range(1, len(nums)):
            diff = target - nums[n]
            if diff in D:
                return [D[diff], n]
            else:
                D[nums[n]] = n
            
        