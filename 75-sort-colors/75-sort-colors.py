class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[2,0,2,1,1,0]
        maxi = max(nums) #2
        L = [0] * (maxi+1) #[0,0,0]
        #print(L)
        for i in nums: #i = 0
            L[i] += 1  #[2,2,2]
        #print(L)#L = [2,2,2]
        j = 0 #0
        k = 0 #0
        while j < len(L): #3
            if L[j] != 0: #j = 0, k = 2
                nums[k] = j #[0,0,2,1,1,0]
                k += 1 #2
                L[j] -= 1  #[0,2,2]
            else:
                #k += 1
                j += 1
            

            
            
            
        
        
        