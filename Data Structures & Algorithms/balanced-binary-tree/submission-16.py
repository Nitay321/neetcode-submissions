# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)

        if not (l and r):
            return False

        l = 0 if not root.left else root.left.height
        r = 0 if not root.right else root.right.height

        root.height = 1 + max(l,r)

        return abs(l - r) <= 1


        