class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        D = {}
        for i in s:
            D[i[-1]] = i
        K = D.keys()
        Keys = list(K)
        for k in range(len(Keys)):
            Keys[k] = int(Keys[k])
        Keys.sort()
        ans = ""
        integers = {"1","2","3","4","5","6","7","8","9","0"}
        for k in Keys:
            r = D[str(k)]
            for j in r:
                if j in integers:
                    ans += " "
                else:
                    ans += j
        mans = ""
        for a in range(len(ans)-1):
            mans += ans[a]
        return mans
        