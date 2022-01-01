class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        S = set()
        n = 1
        l = 1
        while True:
            rem = n % k
            if rem == 0:
                return l
            if rem in S:
                return -1
            n = 10*rem + 1
            l += 1
            S.add(rem)
            
    
            
        
            