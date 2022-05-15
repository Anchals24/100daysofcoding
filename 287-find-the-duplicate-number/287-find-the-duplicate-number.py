class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) -1
        while start <= end:
            mid = (start+end) // 2
            cnt = 0
            for n in nums:
                if n <= mid:
                    cnt += 1
            if cnt > mid:
                end = mid -1
            else:
                start = mid + 1
        return start
                
            