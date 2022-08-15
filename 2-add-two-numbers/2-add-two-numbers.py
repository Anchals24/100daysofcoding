# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertnodes(self, head, tail, newnode):
        if head == None:
            head = newnode
            tail = newnode
        else:
            tail.next = newnode
            tail = tail.next   
        return [head, tail]
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        head = None
        tail = ListNode(-1)
        carry = 0
        while temp1 or temp2:
            if temp1 != None and temp2 != None:
                summ = temp1.val + temp2.val + carry #summ = 2 + 9+ 1
                if summ > 9:
                    last_digit = summ % 10 #2
                    carry = summ // 10  #1
                    newnode = ListNode(last_digit) #2
                else:
                    newnode = ListNode(summ) #3
                    carry = 0
                temp1 = temp1.next
                temp2= temp2.next
            elif temp1 != None:
                summ = temp1.val + carry
                if summ > 9:
                    last_digit = summ % 10 #2
                    carry = summ // 10  #1
                    newnode = ListNode(last_digit)
                else:
                    newnode = ListNode(summ) #3
                    carry = 0 
                temp1 = temp1.next
            elif temp2 != None:
                summ = temp2.val + carry
                if summ > 9:
                    last_digit = summ % 10 #2
                    carry = summ // 10  #1
                    newnode = ListNode(last_digit)
                else:
                    newnode = ListNode(summ) #3
                    carry = 0 
                temp2= temp2.next
            head = self.insertnodes(head,tail, newnode)[0]   
            tail = self.insertnodes(head,tail, newnode)[1]   
        if carry != 0:
            newnode = ListNode(carry)
            self.insertnodes(head,tail, newnode)
        return head
            
            
        
        
            
            