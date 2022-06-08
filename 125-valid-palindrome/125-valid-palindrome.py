import copy
class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = {"1","2","3","4","5","6","7","8","9","0"}
        s1 = ""
        for i in s:
            if i >= "a" and i < "z":
                s1 += i
            elif i >= "A" and i < "Z":
                s1 += i.lower()
            elif i in nums:
                s1 += i
        s2 = ""
        for s in range(len(s1)-1, -1, -1):
            s2 += s1[s]
        if s1 == s2:
            return True
        return False
            
    
        
            
        