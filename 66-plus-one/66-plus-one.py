class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ""
        for d in digits:
            n += str(d)
        n = int(n)
        n = n +1
        ans = []
        while n != 0:
            dig = n % 10
            ans.insert(0,dig)
            n = n // 10
        return ans