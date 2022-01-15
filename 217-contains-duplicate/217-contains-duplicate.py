class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for n in range(len(nums)-1):
            if nums[n] == nums[n+1]:
                return True
        return False
        