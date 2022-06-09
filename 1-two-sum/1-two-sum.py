class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i < j:
                    if nums[i] + nums[j] == target:
                        ans.append(i)
                        ans.append(j)
                        return ans

        