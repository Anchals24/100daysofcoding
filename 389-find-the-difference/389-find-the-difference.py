class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        D1 = {}
        for i in s:
            if i in D1:
                D1[i] += 1
            else:
                D1[i] = 1
        D2 = {}
        for j in t:
            if j in D2:
                D2[j] += 1
            else:
                D2[j] = 1
        for k in t:
            if k not in D1:
                return k
            elif (D1[k] != D2[k]):
                return k
        