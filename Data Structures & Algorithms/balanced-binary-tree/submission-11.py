# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height = 0
        return self.iB(root)

    def iB(self,root):
        if not root:
            return True
        
        a = self.iB(root.left)
        b = self.iB(root.right)

        l = 0 if not root.left else root.left.height
        r = 0 if not root.right else root.right.height

        diff = abs(l - r)

        root.height = 1 + max(l, r)

        return diff<=1 and a and b





        