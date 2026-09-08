# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  
        curr = dummy
        a,b = 0,0 
        left = 0     
        while l1 or l2:
            if l1:
                a = l1.val
            else:
                a = 0
            if l2:
                b = l2.val
            else:
                b = 0
            summ = (a + b + left)
            digit = summ % 10 
            curr.next = ListNode(digit)
            curr = curr.next

            left = summ // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if left == 1:
            curr.next = ListNode(1)


 
        
        return dummy.next
             
            
        