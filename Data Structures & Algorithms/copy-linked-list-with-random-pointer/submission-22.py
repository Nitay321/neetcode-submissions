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
            Id[curr] = Node(curr.val)
            curr = curr.next

        for element in Id:
            if element:
                Id[element].next = Id[element.next]
                Id[element].random = Id[element.random]

        return Id[head]


        