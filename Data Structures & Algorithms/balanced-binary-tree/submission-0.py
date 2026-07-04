# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs through left and right subtrees of each node to get heights
        # if abs(left-right) > 1, return false, else return true
        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            if abs(leftHeight-rightHeight) > 1:
                balanced = False
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return balanced
        