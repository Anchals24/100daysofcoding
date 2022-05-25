class Solution:
    def nextgreaterindex(self, nums, target, i):
        start = i
        end = len(nums) - 1
        larger = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                start = mid + 1
                larger = mid
            elif nums[mid] <= target:
                end = mid - 1
        return larger
    
    def reversee(self, nums, i):
        start = i
        end = len(nums) - 1
        while start < end:
            nums[start] , nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) == 1:
            return nums
        for n in range(len(nums)-2, -1, -1):
            if nums[n] < nums[n+1]:
                largerele = self.nextgreaterindex(nums, nums[n], n+1)
                nums[n] , nums[largerele] = nums[largerele] , nums[n]
                self.reversee(nums, n+1)
                return nums
        nums.reverse()
        return nums
                
        
            
            
            
                
            
            
        
        """
        #Recursion #Bitwise
        Brute-Force 2**n
        > Find all the possible permutations
        > sort 
        > given -> next
        """
        
        
        