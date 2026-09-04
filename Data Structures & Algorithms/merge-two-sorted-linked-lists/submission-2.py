# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       
        if not list1:
             return list2
        if not list2:
            return list1

        curr1 = list1 
        curr2 = list2

        newHead = None
        if curr1.val < curr2.val:
            newHead = curr1
        else:
            nxt2 = curr2.next
            curr2.next = curr1
            newHead = curr2
            curr2 = nxt2

        prev = newHead
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev = curr1
                curr1 = curr1.next
            else:
                nxt = curr2.next
                curr2.next = curr1
                prev.next = curr2
                prev = prev.next
                curr2 = nxt
        if not curr1:
            prev.next = curr2
        return newHead






                



            




        if curr1:
            prev.next = curr2

        return newHead          

        

        

        
         
        