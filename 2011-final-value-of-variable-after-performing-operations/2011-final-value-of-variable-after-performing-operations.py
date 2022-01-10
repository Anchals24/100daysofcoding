class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for o in operations:
            if o == "++X":
                X = X + 1
            elif o == "X++":
                X = X + 1
            elif o == "--X":
                X = X -1
            else:
                X = X -1
        return X
        
        