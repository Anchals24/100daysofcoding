class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        #[1,2,3,4,100,200,201,202,203,204,205]
        if len(nums) == 0:
            return 0
        cnt = 0
        maxi = 0
        for n in range(1, len(nums)): #5
            if nums[n] - nums[n-1] == 1: #nums[3] - nums[2] == 1
                cnt += 1 #3
                maxi = max(maxi, cnt) #3
            elif nums[n] - nums[n-1] > 1:
                cnt = 0
        return maxi + 1
            
            
        