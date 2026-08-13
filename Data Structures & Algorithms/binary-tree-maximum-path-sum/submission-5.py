# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = root.val
        def dfs(node):
            nonlocal maxPath
            if not node:
                return 0
            lSum = max(0, dfs(node.left))
            rSum = max(0, dfs(node.right))
            maxPath = max(maxPath, node.val + lSum + rSum)
            return node.val + max(lSum, rSum)
        dfs(root)
        return maxPath