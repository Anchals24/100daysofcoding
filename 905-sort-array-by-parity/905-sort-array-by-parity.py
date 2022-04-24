class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        first = 0
        last = len(nums) - 1
        while first < last:
            #firstcase: starting -> odd , end -> even
            if nums[last] % 2 == 0 and nums[first] % 2 != 0:
                nums[last], nums[first] = nums[first], nums[last]
                first += 1
                last -= 1
            #secondcase: start -> even, end -> even
            elif nums[last] % 2 == 0 and nums[first] % 2 == 0:
                first += 1
            #thirdcase: start -> even, last-> odd
            elif  nums[last] % 2 != 0 and nums[first] % 2 == 0:
                first += 1
                last -= 1
            #forthcase: start -> odd , end = odd
            elif nums[last] % 2 != 0 and nums[first] % 2 != 0:
                last -= 1
        return nums
                
        