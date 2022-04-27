class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini = 10000000000000000
        ans = []
        for a in range(len(arr) -1):
            if (arr[a+1] - arr[a]) < mini:
                mini = arr[a+1] - arr[a]
        for a in range(len(arr) -1):
            if (arr[a+1] - arr[a]) == mini:
                ans.append([arr[a], arr[a+1]])
        return ans
            
            
            
                    
                    
            
            
        
        