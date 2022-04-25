class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0 
        end = len(arr)-1   
        while (start <= end): 
            mid = start + (end-start) // 2  
            if (mid == len(arr)-1) and (arr[mid] < arr[mid-1]): 
                end = mid -1 
            elif (mid == 0) and (arr[mid] < arr[mid+1]):
                start = mid + 1
            elif (arr[mid-1] < arr[mid]) and (arr[mid] > arr[mid+1]): 
                return mid
            elif (arr[mid] < arr[mid-1]): 
                end = mid -1 #end = 1
            elif (arr[mid] < arr[mid+1]):
                start = mid + 1
            
            
            
            #[1,3,5,18,13,12,7]
            """
            [8,3,2,1] or [1,2,3,8]
            
            """
            
            
            
            
            
        
        