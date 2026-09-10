# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = collections.deque()
        dq.append(root)
        res = []
        while dq:
            last_level_node = None
            for i in range(len(dq)):
                node = dq.popleft()
                if node:
                    last_level_node = node
                    dq.append(node.left)
                    dq.append(node.right)
                
            if last_level_node:
                res.append(last_level_node.val)
        return res
        
        