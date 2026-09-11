# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
 
        def dfs(root, maxV):
            if not root:
                return 0
            b = 0
            if root.val >= maxV:
                b = 1
                maxV = root.val
            
            return b + dfs(root.left, maxV) + dfs(root.right, maxV) 

        return dfs(root,root.val)
        