class Solution:
    def countPoints(self, rings: str) -> int:
        #"B0R0G0R9R0B0G0"
        L = []
        for l in range(10):
            l = set()
            L.append(l)
        #L = [{"B","R"}, {}, {}, {}, {},{},{},{},{},{}]
        N = {"0","1","2","3","4","5","6","7","8","9"}
        ans = 0 
        for r in range(len(rings)): #(14)
            #r = 3
            if rings[r] in N:#rings[1] == "0" 
                L[int(rings[r])].add(rings[r-1]) 
        for l in L:
            if len(l) == 3:
                ans += 1
        return ans
                
                    
                    
            
        
        