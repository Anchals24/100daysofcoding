class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < 2:
            for n in nums:
                ans.append(n)
            i += 1
        return ans
        