class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        for n in nums:
            if n in D:
                D[n] += 1
            else:
                D[n] = 1
        ans = []
        while k > 0:
            keyMax = max(D.items(), key = operator.itemgetter(1))[0]
            ans.append(keyMax)
            D[keyMax] = -1
            k -= 1
        return ans

        