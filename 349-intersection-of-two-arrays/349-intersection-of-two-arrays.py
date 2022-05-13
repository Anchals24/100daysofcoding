class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        D = {}
        for n in nums1:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1
        Set = set()
        for i in nums2:
            if i in D and D[i] > 0:
                Set.add(i)
                D[i] -= 1
        return Set
                
        
        