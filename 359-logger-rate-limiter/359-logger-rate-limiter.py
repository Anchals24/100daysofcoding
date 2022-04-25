class Logger:

    def __init__(self):
        self.logger = {}
        
    #["Logger","shouldPrintMessage","shouldPrintMessage"]
    #[[],[100,"bug"],[111,"bug"]]
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.logger:
            if self.logger[message] + 10 <= timestamp:
                self.logger[message] = timestamp
                return True
            else:
                return False
        elif message not in self.logger:
            self.logger[message] = timestamp #{"bug" : 100}
            return True
            
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


"""
Pseudo Code:
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]







"""