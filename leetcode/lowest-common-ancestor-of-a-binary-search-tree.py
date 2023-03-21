# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        a, b = min(p.val, q.val), max(p.val, q.val)
        while root:
            if a > root.val:
                root = root.right
            elif b < root.val:
                root = root.left
            else:
                return root