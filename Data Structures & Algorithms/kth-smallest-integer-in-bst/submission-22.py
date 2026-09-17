# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        flag = True
        while stack:
            node = stack[-1]
            if node:
                stack.append(node.left)
            else:
                stack.pop()
                k -= 1
                node = stack.pop()
                if k == 0:
                    return node.val
                stack.append(node.right)
        return -1





           


            
            




        