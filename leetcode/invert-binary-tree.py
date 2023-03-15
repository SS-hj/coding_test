# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def move(tn):
            if tn:
                tn.left, tn.right = tn.right, tn.left
                move(tn.left)
                move(tn.right)
                return root
            else:
                return None
        return move(root)