import heapq as heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for s in range(len(stones)):
            stones[s] = stones[s] * -1
        heap.heapify(stones)
        while len(stones) > 1:
            y = heap.heappop(stones) * -1
            x = heap.heappop(stones) * -1
            if x != y:
                heap.heappush(stones, (y-x) * -1)
        if len(stones) == 0:
            return 0
        return stones[0] * -1
        
        
                
            
        
        