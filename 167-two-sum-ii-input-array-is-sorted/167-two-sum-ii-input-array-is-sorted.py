class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)#4
        start = 0 #1
        last = n-1 #3
        ans = []
        while start <= last:
            if numbers[start] + numbers[last] == target:
                ans.append(start + 1)
                ans.append(last + 1 )
                return ans
            elif numbers[start] + numbers[last] > target:
                last -= 1
            elif numbers[start] + numbers[last] < target:
                start += 1
        
            
                
        