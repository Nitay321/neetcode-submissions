# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.r_l(None, head)



    def r_l(self, prev: Optional[ListNode], curr: Optional[ListNode]) -> Optional[ListNode]:
        if not curr:
            return prev
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr= nxt
        return self.r_l(prev, curr)
     



    
        


        