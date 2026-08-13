# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            lSum = max(0, dfs(node.left))
            rSum = max(0, dfs(node.right))
            maxSum = max(maxSum, node.val + lSum + rSum)
            return node.val + max(lSum, rSum)
        dfs(root)
        return maxSum