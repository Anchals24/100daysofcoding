class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals , key = lambda x:x[0])
        start = -1000000
        end = -1000000
        mergedintervals = []
        for i in range(len(intervals)):
            temp = intervals[i]
            if temp[0] > end:
                if i != 0:
                    mergedintervals.append([start , end])
                start = temp[0]
                end = temp[1]
            else:
                end = max(end , temp[1])

        if end != -1000000 and [start, end] not in mergedintervals:
            mergedintervals.append([start,end])
        #print("Merged intervals are >> ")
        return mergedintervals
        