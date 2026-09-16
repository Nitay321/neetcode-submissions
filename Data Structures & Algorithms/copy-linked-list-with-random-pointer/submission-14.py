"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        Id = {None:None}
        curr = head

        while curr:
            newNode = Node(curr.val)
            Id[curr] = newNode
            curr = curr.next


        curr = head 

        while curr:
            Id[curr].next = Id[curr.next]
            Id[curr].random = Id[curr.random]
            curr = curr.next

        return Id[head] 


        


     
        


        







        