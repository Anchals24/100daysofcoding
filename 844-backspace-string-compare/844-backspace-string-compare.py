from collections import deque
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S1 = deque()
        S2 = deque()
        news = ""
        newt = ""
        for i in s:
            if i == "#" and len(S1) == 0:
                continue
            if i == "#":
                S1.pop()
            else:
                S1.append(i)
        for j in t:
            if j == "#" and len(S2) == 0:
                continue    
            if j == "#":
                S2.pop()
            else:
                S2.append(j)
        while S1:
            t = S1.pop()
            news += t
        while S2:
            t1 = S2.pop()
            newt += t1
        if news == newt:
            return True
        return False
        
        
        