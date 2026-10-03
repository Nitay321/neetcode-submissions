# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxD = 0
        def calHeight(node):
            if not node:
                return 0
            
            l = calHeight(node.left)
            r = calHeight(node.right)
            self.maxD = max(self.maxD, l + r)
            return 1 + max(l,r)

        calHeight(root)
        return self.maxD
        