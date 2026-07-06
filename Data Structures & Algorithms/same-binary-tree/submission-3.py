# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p1 = []
        q1 = []
        def dfs(node, traversal):
            if not node:
                traversal.append(None)
                return
            traversal.append(node.val)
            dfs(node.left, traversal)
            dfs(node.right, traversal)
        
        dfs(p, p1)
        dfs(q, q1)
        return p1 == q1