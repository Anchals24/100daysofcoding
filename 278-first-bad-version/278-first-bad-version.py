# The isBadVersion API is already defined for you.
#def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        ans = 0
        while low <= high:
            mid = (low+high)//2
            if isBadVersion(mid) == True:
                ans = mid
                high = mid-1 
            elif isBadVersion(mid) != True:
                low = mid + 1
        return ans
                
            
                
        
            
        """
        low = 0
        high = len(a) -1
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                low = mid + 1
            if arr[mid] > target:
                high = mid - 1
            
        """
            
        