# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        left = 0
        while l1 and l2:
            summ = (l1.val + l2.val + left) 
            num = summ % 10 
            left = summ // 10
            curr.next = ListNode(num)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        l = l1 if l1 else l2
        while l:
            summ = l.val + left
            num = summ % 10 
            left = summ // 10

            curr.next = ListNode(num)
            curr = curr.next
            l = l.next

        if left == 1:
            curr.next = ListNode(left)

        return dummy.next

        



            
             
            


        