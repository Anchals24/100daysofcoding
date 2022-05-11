import heapq as heap
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        D = {}
        for w in words:
            if w in D:
                D[w] += 1
            else:
                D[w] = 1
        ans = []
        Heap = []
        for key,value in D.items():
            Heap.append((value * -1, key))
        heap.heapify(Heap)
        while k > 0:
            largest = heap.heappop(Heap)
            ans.append(largest[1])
            k -= 1
        return ans
            
            
            
            
            
            
        
            
            
        
            
        
        
        
        