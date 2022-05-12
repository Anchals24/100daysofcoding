class Solution:
    def mySqrt(self, x: int) -> int:
        #2*2 = 4
        #3*3 = 9
        if x == 0:
            return 0
        i = 1
        prev = 1
        j = 1
        #x = 16
        while True:
            i = j * j #16
            if i == x: 
                return j
            if i > x:
                return prev
            prev = j #3
            j += 1 #4
        
        
            
            
        