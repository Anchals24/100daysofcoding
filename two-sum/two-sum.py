class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for n in range(len(nums)):
            sub = target - nums[n]
            if sub in D:
                return [D[sub] , n]
            D[nums[n]] = n
        