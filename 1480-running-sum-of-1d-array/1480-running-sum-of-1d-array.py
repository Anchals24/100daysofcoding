class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Ans = []
        Ans.append(nums[0])
        for i in range(1 , len(nums)):
            nextt = Ans[-1] + nums[i]
            Ans.append(nextt)
        return Ans
            
        