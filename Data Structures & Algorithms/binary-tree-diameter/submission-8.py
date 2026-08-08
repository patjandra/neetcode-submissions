# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = 0
        def dfs(node):
            nonlocal d
            if not node:
                return 0
            lh = dfs(node.left)
            rh = dfs(node.right)
            d = max(d, lh+rh)
            return 1 + max(lh, rh)
        dfs(root)
        return d