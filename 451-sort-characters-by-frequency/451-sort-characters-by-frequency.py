import heapq as heap
class Solution:
    def frequencySort(self, s: str) -> str:
        D = {}
        for i in s:
            if i in D:
                D[i] += 1
            else:
                D[i] = 1
        h = []
        ans = ""
        for key,value in D.items():
            h.append((value * -1, key))
        heapq.heapify(h)
        #print(h)
        #[(-2, 'e'), (-1, 'r'), (-1, 't')]
        lenn = len(s)
        leng = 0
        while leng != lenn:
            largest = heapq.heappop(h)
            for i in range(largest[0] * -1):
                ans += largest[1]
                leng += 1
        return ans
            
            
            
            
        
        
        