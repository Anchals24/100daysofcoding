# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def llength(self, head):
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cntA = self.llength(headA)
        cntB = self.llength(headB)
        temp1 = headA
        temp2 = headB
        if cntA > cntB:
            diff = abs(cntA- cntB)
            while diff:
                temp1 = temp1.next
                diff -= 1
        elif cntA < cntB:
            diff = cntB - cntA
            while diff:
                temp2 = temp2.next
                diff -= 1
        while temp1:
                if temp1 == temp2:
                    return temp1
                temp1 = temp1.next
                temp2 = temp2.next
        return None
                
            
        
        