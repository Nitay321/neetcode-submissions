# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def treeToString(root):
            if not root:
                return ",#"

            return f",{root.val}" + treeToString(root.left) + treeToString(root.right)
        
        tree = treeToString(root)
        subTree = treeToString(subRoot)
        print(subTree + "   " + tree)

        return subTree in tree
            
        