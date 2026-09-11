# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        root.maxV = root.val
        return self.gN(root)


    def gN(self, root: TreeNode) -> int:
        b = 0
        if not root:
            return 0
            
        maxV = root.maxV 
        if root.val >= maxV:
            b = 1
            maxV = root.val

        if root.left:
            root.left.maxV = maxV

        if root.right:
            root.right.maxV = maxV

        return b + self.gN(root.left) + self.gN(root.right)


            
            

            
        

                
 




    




        
        