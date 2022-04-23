class Solution:
    def fib(self, n: int) -> int:
        ans = [0,1]
        #[0,1,1,2,3]
        if n == 0:
            return ans[0]
        elif n == 1:
            return ans[1]
        #n = 4
        for i in range(1, n): #(2, 4) 3
            new = ans[-1] + ans[-2] #new = 1 + 0 = 1 #ans = [0,1,1]
            ans.append(new)
        return ans[-1]
            
            