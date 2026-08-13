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
            lSum = dfs(node.left)
            rSum = dfs(node.right)
            maxPath = max(maxPath, node.val + lSum + rSum, node.val + lSum, node.val + rSum, node.val)
            return max(node.val, node.val + lSum, node.val + rSum)
        dfs(root)
        return maxPath