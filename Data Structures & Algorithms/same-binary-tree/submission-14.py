# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(tree, lst):
            if not tree:
                lst.append(None)
                return
            lst.append(tree.val)
            dfs(tree.left, lst)
            dfs(tree.right, lst)
            return lst
        return dfs(p, []) == dfs(q, [])