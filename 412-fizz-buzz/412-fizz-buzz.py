class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        Ans = [0] * (n+1)
        #print(Ans)
        for i in range(1 , n+1):
            if i % 3 == 0 and i % 5 == 0:
                Ans[i] = "FizzBuzz"
            elif i % 3 == 0:
                Ans[i] = "Fizz"
            elif i % 5 == 0:
                Ans[i] = "Buzz"
            else:
                Ans[i] = str(i)
        Ans.pop(0)
        return Ans
                
            
                
        