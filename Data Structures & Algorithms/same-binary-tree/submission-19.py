# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        s = [[p, q]]

        while s:
            p, q = s.pop()
            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            s.append([p.right, q.right])
            s.append([p.left, q.left])
        return True