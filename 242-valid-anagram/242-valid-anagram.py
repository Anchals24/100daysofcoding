class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        DC1 = {}
        DC2 = {}
        for i in s:
            if i in DC1:
                DC1[i] += 1
            else:
                DC1[i] = 1
        for j in t:
            if j in DC2:
                DC2[j] += 1
            else:
                DC2[j] = 1
        for k in s:
            if k not in DC2.keys():
                return False
            if DC1[k] != DC2[k]:
                return False
        return True
        