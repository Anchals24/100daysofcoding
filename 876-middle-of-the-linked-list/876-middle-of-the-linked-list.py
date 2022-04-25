# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt//2 
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cntt = self.count(head)
        temp = head
        while cntt:
            temp = temp.next
            cntt -= 1
        return temp
            
        
        
        