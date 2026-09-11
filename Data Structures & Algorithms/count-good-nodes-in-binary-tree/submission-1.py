# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = []
        stack.append((root,root.val))
        count = 0

        while stack:
            curr = stack.pop()
            node, maxV  = curr[0], curr[1]
            if node:
                if node.val >= maxV:
                    count += 1
                    maxV = node.val
                
                stack.append((node.left, maxV))
                stack.append((node.right, maxV))

        return count











        