class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        la = 0
        ln = len(nums)
        i = 0
        while la != ln:
            if i <= ln:
                ans.append(nums[i])
                la += 1
            if n <= ln:
                ans.append(nums[n])
                la += 1
            i += 1
            n += 1
        return ans