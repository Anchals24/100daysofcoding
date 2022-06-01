class Solution:
    def signFunc(self, product):
        if product > 0:
            return 1
        elif product < 0:
            return -1
        if product == 0:
            return 0
            
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product = n * product 
        return self.signFunc(product)
            