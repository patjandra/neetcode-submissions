# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # dfs, append, if leaf compute sum, pop, return
        # if not node, pop and return
        sums = []
        stack = []

        if not root:
            return False

        def dfs(node):
            if not node:
                return
            
            stack.append(node.val)
            if not node.left and not node.right:
                sums.append(sum(stack))
                stack.pop()
                return
            dfs(node.left)
            dfs(node.right)
            stack.pop()
        dfs(root)

        if targetSum in sums:
            return True
        return False
        