class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maxi = max(arr)
        m = maxi
        D = {}
        for a in arr:
            D[a] = None
        #print(D)
        ans = []
        for i in range(1, maxi+1):
            if i not in D:
                ans.append(i)
        #print(ans)
        if len(ans) == 0:
            while k != 0:
                m += 1
                ans.append(m)
                k -= 1
            return ans[k-1]
        elif len(ans) < k:
            diff = k - len(ans)
            while diff != 0:
                m += 1
                ans.append(m)
                diff -= 1
            return ans[k-1]
        else:
            return ans[k-1]
                
            
        
                
                
        
        
                
                    
                
        
        """
        arr[1] = 0      -> 1
        arr[2] = 1 , 0
        arr[3] = 2 , 1 
        arr[4] = 3 , 2
        arr[5] = 4       -> 2
        arr[6] = 5       -> 3
        arr[7] = 6      
        arr[8] = 7 , 3   
        arr[9] = 8      -> 4
        arr[10] = 9     -> 5
        arr[11] = 10 , 4  
        """
        