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
                return [True, 0]
            heightL = dfs(node.left)
            heightR = dfs(node.right)
            isBalanced = heightL[0] and heightR[0] and abs(heightL[1] - heightR[1]) <= 1
            return [isBalanced, 1 + max(heightL[1], heightR[1])]
        return dfs(root)[0]