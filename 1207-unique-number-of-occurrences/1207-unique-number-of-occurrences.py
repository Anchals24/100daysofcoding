class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Freq = {}
        for a in arr:
            if a in Freq:
                Freq[a] += 1
            else:
                Freq[a] = 1
        Values = Freq.values()
        V = list(Values)
        V.sort()
        #print(V)
        for v in range(1, len(V)):
            if V[v] == V[v-1]:
                return False
        return True
            
        