# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([(root,0)])
        res = collections.defaultdict(list)
        while q:
            node,level = q.popleft()
            if node:
                res[level].append(node.val)
                q.append((node.left,level+1))
                q.append((node.right,level+1))

        return list(res.values())



            