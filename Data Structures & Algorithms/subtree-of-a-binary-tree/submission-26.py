# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root,subRoot):
            if root and subRoot:
                if root.height == subRoot.height:
                    return self.equels(root,subRoot)
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
            return False

        self.calHeight(root)
        self.calHeight(subRoot)
        return dfs(root,subRoot)


    def equels(self, root, subRoot):
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot):
            return False
        if root.val != subRoot.val:
            return False

        return self.equels(root.left,subRoot.left) and self.equels(root.right,subRoot.right) 

    def calHeight(self,root):
        if root:
            self.calHeight(root.left)
            self.calHeight(root.right)
            a = 0 if not root.left else root.left.height
            b = 0 if not root.right else root.right.height
            root.height = 1 + max(a,b)
        