class Solution:
    def mySqrt(self, x: int) -> int:
        #2*2 = 4
        #3*3 = 9
        if x == 1:
            return 1
        if x == 0:
            return 0
        low = 1
        high = x-1
        #8
        while low <= high: #1 < 7
            mid = (low+high)//2 #3
            if mid * mid == x:
                return mid
            if mid * mid > x:
                high = mid - 1 #3
            if mid * mid < x:
                low = mid + 1 #3
        return high
            
            
        
        """
        low = 0
        high = len(arr)-1
        while low < high:
            mid = (low + high)// 2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                high = mid - 1
            if arr[mid] < target:
                low = mid + 1
        return -1
        """
        
        
            
            
        