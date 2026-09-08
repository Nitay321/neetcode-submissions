# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        curr = head

        while curr:
            curr = curr.next
            length += 1

        count = length - n
        print(count)

        dummy = ListNode()
        prev, curr = dummy, head
        prev.next = head
        i = 0

        while curr:
            if i == count:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            i+=1

        head = dummy.next
        return head



        
        