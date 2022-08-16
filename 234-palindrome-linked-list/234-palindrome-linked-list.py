# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def notexactcopy(self, head, newnode):
        if head is None:
            head = newnode
        else:
            newnode.next = head
            head = newnode
        return head
        
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head1 = None
        temp = head
        while temp:
            newnode = ListNode(temp.val) #1
            head1 = self.notexactcopy(head1, newnode)
            temp = temp.next
        t1 = head
        t2 = head1
        while t1:
            if t1.val != t2.val:
                return False
            t1 = t1.next
            t2 = t2.next
        return True
        
        
            
        
        
        
        