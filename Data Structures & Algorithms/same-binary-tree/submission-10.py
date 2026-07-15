# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, l):
            if not node:
                l.append(None)
                return
            l.append(node.val)
            dfs(node.left, l)
            dfs(node.right, l)
            return l
        return dfs(p, []) == dfs(q, [])