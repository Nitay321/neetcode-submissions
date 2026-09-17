# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        slow, fast = dummy, head
        start = slow
       
        while fast.next:
            if n > 1:
                fast = fast.next
                n -= 1
            else:
                slow = slow.next
                fast = fast.next

                
        slow.next = slow.next.next

        return start.next


        