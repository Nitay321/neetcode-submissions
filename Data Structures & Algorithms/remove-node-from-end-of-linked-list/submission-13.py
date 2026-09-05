# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        length = 0

        while curr:
            curr = curr.next
            length+=1

        target = length - n
        

        if target == 0:
            nxt = head.next
            head.next = None
            head = nxt
        else:
            count = 1
            curr = head.next
            prev = head
            while curr:
                if count == target:
                    nxt = curr.next
                    curr.next = None
                    prev.next = nxt
                    break
                prev = curr
                curr = curr.next
                count+=1
        return head


        
        




        