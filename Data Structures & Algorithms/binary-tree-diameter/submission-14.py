# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.DBT(root)
        return self.res


    def DBT(self, root):
        if not root:
            return 0

        d1 = self.DBT(root.left)
        d2 = self.DBT(root.right)

        self.res = max(self.res, d1 + d2)

        return max(d1,d2) + 1

