# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        D = {}
        temp = head
        while temp:
            if temp in D:
                return temp
            else:
                D[temp] = None
            temp = temp.next
        return None
        