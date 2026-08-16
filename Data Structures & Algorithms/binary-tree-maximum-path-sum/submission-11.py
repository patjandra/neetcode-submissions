# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, -math.inf)
            LSum, LMax = dfs(node.left)
            RSum, RMax = dfs(node.right)
            return ((node.val + max(0, LSum, RSum)), max((node.val + max(0, LSum) + max(0, RSum)), LMax, RMax))
        return dfs(root)[1]