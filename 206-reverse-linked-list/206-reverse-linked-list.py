# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        h = head #1
        temp = head.next #2
        prev = head #1
        while temp: #2
            t = temp #2
            temp = temp.next #3
            t.next = prev #2.next = 1
            prev = t #2
            h.next = None 
        head = t
        return head
            
        