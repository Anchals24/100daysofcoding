class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ""
        w2 = ""
        for w in word1:
            w1 += w
        for v in word2:
            w2 += v
        if w1 == w2:
            return True
        else:
            return False
        