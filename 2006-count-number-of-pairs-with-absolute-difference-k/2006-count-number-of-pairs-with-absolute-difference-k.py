class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(1 , len(nums)):
                if i < j and abs(nums[i] - nums[j]) == k:
                    cnt += 1
        return cnt
        