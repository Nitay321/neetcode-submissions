# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.calHeight(root)
        self.calHeight(subRoot)

        def iS(root,subRoot):
            if not root:
                return False
            if root.height < subRoot.height:
                return False
            if root.height > subRoot.height:
                return iS(root.left, subRoot) or iS(root.right, subRoot)
        
            return self.isEquel(root,subRoot)

        return iS(root,subRoot)



    def calHeight(self,root):
        if root:
            self.calHeight(root.left)
            self.calHeight(root.right)
            a = 0 if not root.left else root.left.height
            b = 0 if not root.right else root.right.height

            root.height = 1 + max(a, b)
            
        
    
        

   

            

            



    def isEquel(self, root, subRoot):
        if not subRoot and not root:
            return True
        if not subRoot or not root:
            return False
        if root.val != subRoot.val:
            return False

        return self.isEquel(root.left, subRoot.left) and self.isEquel(root.right, subRoot.right)

    


            
        