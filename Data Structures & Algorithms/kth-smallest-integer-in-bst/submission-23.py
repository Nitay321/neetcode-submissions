# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.k_num = None

        def inOrder(node,k):

            if node and not self.k_num:
                inOrder(node.left,k)
                self.counter += 1
                print(self.counter,k)
                if self.counter == k:        
                    self.k_num = node.val
                
                inOrder(node.right,k)

            
       
        inOrder(root, k) 
        return self.k_num

        

       

        
        