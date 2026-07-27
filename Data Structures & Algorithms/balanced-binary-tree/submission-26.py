# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [0, True]
            lh = dfs(node.left)
            rh = dfs(node.right)
            balanced = lh[1] and rh[1] and abs(rh[0] - lh[0]) <= 1
            return [1 + max(lh[0], rh[0]), balanced]
        return dfs(root)[1]