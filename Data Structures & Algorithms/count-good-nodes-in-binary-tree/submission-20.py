import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def gN(node,max_value_so_far, count):
            if node:
                if node.val >= max_value_so_far:
                    max_value_so_far = node.val
                    self.count += 1
                
                gN(node.left,max_value_so_far,self.count) 
                gN(node.right,max_value_so_far,self.count)
        
        gN(root,-math.inf, self.count)
        return self.count

    

        