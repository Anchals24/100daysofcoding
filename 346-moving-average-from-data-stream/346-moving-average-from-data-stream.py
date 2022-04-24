class MovingAverage:

    def __init__(self, size: int):
        self.windowsize = size
        self.curr_size = 0
        self.prev_avg = 0
        self.prev_size = 0
        self.values = []
        self.minus = 0
        
    def next(self, val: int) -> float:
        self.curr_size += 1
        self.values.append(val)
        if self.curr_size <= self.windowsize:
            self.prev_avg = (self.prev_avg * self.prev_size + val)/(self.curr_size)
            self.prev_size += 1
        elif self.curr_size > self.windowsize:
            self.prev_avg = (self.prev_avg * self.windowsize - self.values[self.minus] + val)/ self.windowsize
            self.minus += 1
        return self.prev_avg
            
            
            
            
            
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

"""
pseudo code:

step1: w.size = 3, sod = 1, 1/1
1/1 = 1.0
prevavg * prevsize + newnum/ currsize
1.0 * 1 + 10/ 2
step2: w.size = 3, sod = 2, sum/2
step3: w.size == stream.size, sum/size
step4: stream -> initial pos pop -> next new element insert
(4.66667 *3 - 1 + 5)=  sum/size
1 + 10 + 3/ 3
avg * 3 - 1 + 5 = /3
"""