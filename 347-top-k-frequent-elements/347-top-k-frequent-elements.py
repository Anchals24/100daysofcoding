import heapq as heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        for n in nums:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1
        max_heap = []
        S = set()
        ans = []
        for n in range(len(nums)):
            if nums[n] not in S:
                heap.heappush(max_heap, (-1 * D[nums[n]], nums[n]))
            S.add(nums[n])
        while k > 0:
            mini = heap.heappop(max_heap)  #(cnt, num)
            ans.append(mini[1])
            k -= 1
        return ans
            
            
            
        
            
        
        