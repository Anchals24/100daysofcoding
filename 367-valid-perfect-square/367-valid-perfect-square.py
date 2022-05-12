class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low = 1
        high = num // 2 
        while low <= high:
            mid = (low+high) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                high = mid - 1  
            elif mid * mid < num:
                low = mid + 1
        return False
                
        