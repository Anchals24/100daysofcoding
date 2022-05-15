import sys
class MinStack:

    def __init__(self):
        self.s1 = []
        
    #self.s1 = [(2,2), (1, 1)]

    def push(self, val: int) -> None:
        if len(self.s1) == 0:
            self.s1.append((val,val ))
        else:
            self.s1.append((val, min(self.s1[-1][1], val)))    
        
    def pop(self) -> None:
        self.s1.pop()
        

    def top(self) -> int:
        if len(self.s1) != 0:
            return self.s1[-1][0]
            
    def getMin(self) -> int:
        return self.s1[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()