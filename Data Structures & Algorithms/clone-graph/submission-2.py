"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        Id = {None:None}
        head = node
        q = collections.deque()
        q.append(node)

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node and node not in Id:
                    Id[node] = Node(node.val)
                
                    for neb in node.neighbors:
                        q.append(neb)
        
        for node in Id:
            nebs = []
            if not node:
                continue
            for neb in node.neighbors:
                nebs.append(Id[neb])

            Id[node].neighbors = nebs
        
        return Id[head]

            





        