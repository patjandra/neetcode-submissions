# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        t1 = []
        t2 = []

        def dfs(lst, root):
            if not root:
                lst.append(0)
                return
            lst.append(root.val)
            dfs(lst, root.left)
            dfs(lst, root.right)

        dfs(t1, p)
        dfs(t2, q)
        return t1 == t2