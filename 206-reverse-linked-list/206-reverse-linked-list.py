# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #1
        temp = head
        t = None
        while temp: #2
            t = temp #2
            temp = temp.next #3
            t.next = prev #2.next = 1
            prev = t
        head = t
        return head
            
        