class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs)
        lmini = len(mini)
        ans = ""
        for i in range(lmini):
            for string in strs:
                if string[i] != mini[i]:
                    return ans
            ans += mini[i]
        return ans
            
        