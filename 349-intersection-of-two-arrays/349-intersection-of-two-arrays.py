class Solution:
    def Binarysearch(self, arr, target):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = len(nums1)
        l2 = len(nums2)
        S = set()
        nums1.sort()
        nums2.sort()
        if l1 < l2:
            for i in nums1:
                if self.Binarysearch(nums2, i) == True:
                    S.add(i)
        else:
            for i in nums2:
                if self.Binarysearch(nums1, i) == True:
                    S.add(i)
        return S
                
                
        
                
        
        