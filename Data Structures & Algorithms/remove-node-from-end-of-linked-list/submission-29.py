# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left, right = head, head
        count = 0
        while right:
            right = right.next
            count += 1
            if count == n:
                break
                
        if not right:
            return head.next

        while right.next:
            right=right.next
            left=left.next
        
        left.next = left.next.next
        return head



            



        

        