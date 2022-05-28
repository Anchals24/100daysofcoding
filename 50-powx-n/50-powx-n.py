class Solution:
    def myPow(self, x: float, n: int) -> float: #2 n = 3
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            y = self.myPow(x , n//2)
            return y * y
        if n > 0:
            return x * self.myPow(x, n-1) 
        if n < 0: 
            return 1 / x * self.myPow(x, n+1)
            
        
        
        
        
        
        
    
    
    
        
        