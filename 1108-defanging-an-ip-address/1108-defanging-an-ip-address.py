class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for a in address:
            if a == ".":
                ans += "[.]"
            else:
                ans += a
        return ans
        