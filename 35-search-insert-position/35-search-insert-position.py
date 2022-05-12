class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        [1,3,5,6]
        2
        """
        low = 0
        high = len(nums)-1 #3
        ans = high + 1
        while low <= high: #0<3
            mid = (low+high)//2 #1
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid -1 #0
                ans = mid
            if nums[mid] < target:
                low = mid + 1 #low = 4
        return ans 
        
        
        
        
        
        
        
        
        
        
        """
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                high = mid -1
            if arr[mid] < target:
                low = mid + 1
            
        """
        