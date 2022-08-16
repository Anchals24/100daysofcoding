# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        D = {}
        temp1 = headA
        while temp1:
            D[temp1] = None
            temp1 = temp1.next
        temp2 = headB
        while temp2:
            if temp2 in D:
                return temp2
            temp2 = temp2.next
        return None
        
        