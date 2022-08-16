# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        D = {}
        temp = head
        while temp:
            if temp in D:
                return True
            else:
                D[temp] = None
            temp = temp.next
        return False
        
        