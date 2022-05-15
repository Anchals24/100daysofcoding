from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        S = deque() #
        D = {}
        news = ""
        for i in range(len(s)): #8
            if s[i] == "(":
                S.append((s[i], i))
            elif s[i] == ")" and len(S) != 0:
                S.pop()
            elif s[i] == ")" and len(S) == 0:
                D[i] = None
        while S:
            t = S.pop()
            D[t[1]] = None
        for i in range(len(s)):
            if i not in D:
                news += s[i]
        return news
            
            
        
        
        
        