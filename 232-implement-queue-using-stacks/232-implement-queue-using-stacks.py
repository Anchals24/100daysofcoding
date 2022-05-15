class MyQueue:

    def __init__(self):
        self.S1 = [] #[1,2]
        self.S2 = [] #[2]
        
    def push(self, x: int) -> None:
        self.S1.append(x)
        
    def peek(self) -> int:
        if len(self.S2) != 0:
            return self.S2[-1]
        else:
            return self.S1[0] #[1]
        
    def pop(self) -> int:
        if len(self.S2) == 0:
            while len(self.S1) != 0:
                temp = self.S1.pop() #2
                self.S2.append(temp) 
        return self.S2.pop()
        
    def empty(self) -> bool:
        if len(self.S1) == 0 and len(self.S2) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()