from collections import deque 
from collections import defaultdict 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = deque([])
        dq.append((root,0))
        res = []
        dictt = defaultdict(list)
        while dq:
            curr = dq.popleft()
            node, level = curr[0],curr[1]
            if node:
                dictt[level].append(node.val)
                dq.append((node.left,level+1))
                dq.append((node.right,level+1))
        
        return list(dictt.values())
       


        

        


        