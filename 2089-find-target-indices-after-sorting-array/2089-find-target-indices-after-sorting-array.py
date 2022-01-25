class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for n in range(len(nums)):
            if nums[n] == target:
                ans.append(n)
        return ans