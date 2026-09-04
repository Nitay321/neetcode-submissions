# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        dictt = {}

        i = 0
        while curr:
            if curr not in dictt:
                dictt[curr] = i
                curr = curr.next
            else:
                return True
        return False
                

            
           
        

        