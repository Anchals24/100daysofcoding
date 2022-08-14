# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def lenn(self, head):
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lenn(head) #2
        #print(length)
        remove = length - (n-1) #2-(2-1) = 2-1 = 1
        if remove == 1:
            head = head.next
            return head
        temp = head
        cnt = 0
        while temp:
            cnt += 1 #1
            if cnt == remove - 1:
                temp.next = temp.next.next
            temp = temp.next
        return head
        