from collections import deque
class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        pos = 0
        speed = 1
        Q = deque()
        Q.append((pos, speed, 0)) 
        while Q:
            temp = Q.popleft()  
            
            if temp[0] + temp[1] == target: 
                return temp[2] + 1 
            Q.append((temp[0] + temp[1] , temp[1] * 2, temp[2] + 1 ))
            if temp[0] + temp[1] > target and temp[1] > 0:
                Q.append((temp[0], -1, temp[2] +1)) 
            if temp[0] + temp[1] < target and temp[1] < 0:
                Q.append((temp[0], 1, temp[2] +1 ))
                
            
            
            
            
            
            
            
        
        
        
        
        
        
        