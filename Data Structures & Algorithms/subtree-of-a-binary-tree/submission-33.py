# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def getHeight(node):
            if node:
                getHeight(node.left)
                getHeight(node.right)
                l = 0 if not node.left else node.left.height
                r = 0 if not node.right else    node.right.height
                node.height = 1+max(l, r)

        def isEquel(node, subNode):
            if not node and not subNode:
                return True
            elif node and not subNode:
                return False
            elif subNode and not node:
                return False
            elif node.val != subNode.val:
                return False
            else:
                return isEquel(node.left, subNode.left) and isEquel(node.right, subNode.right)
    

        def dfs(node, subRoot):
            if not node or node.height < subRoot.height:
                return False
            elif node.height > subRoot.height:
                return dfs(node.left,subRoot) or dfs(node.right,subRoot) 
            else:
                return isEquel(node, subRoot)

                
        if not subRoot:
            return True 
        getHeight(root)
        getHeight(subRoot)

        return dfs(root,subRoot)
    



        