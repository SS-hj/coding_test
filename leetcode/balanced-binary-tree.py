# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: 
                return 0
            left, right = dfs(root.left), dfs(root.right)
            return float('inf') if abs(left - right) > 1 else max(left, right) + 1
        
        return dfs(root) != float('inf')