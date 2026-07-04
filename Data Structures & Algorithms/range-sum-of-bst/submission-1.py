# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            currSum = 0
            if low <= node.val <= high:
                currSum += node.val
            currSum += dfs(node.left) + dfs(node.right)
            return currSum
            
        return dfs(root)