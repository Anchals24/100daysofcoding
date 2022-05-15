from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        Pairs = {('(',')'): None, ('[',']'): None ,  ('{','}'): None }
        Open = ("[", "(", "{")
        S = deque()
        for i in s:
            if i in Open:
                S.append(i)
            if i not in Open and len(S) == 0:
                return False
            if i not in Open:
                t = S.pop()
                if (t,i) not in Pairs:
                    return False
        if len(S) != 0:
            return False
        return True
                    
                
                
        