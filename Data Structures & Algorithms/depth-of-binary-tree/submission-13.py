# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = [(root, 1)]
        depth = 0
        while s:
            node, currDepth = s.pop()
            if node:
                depth = max(depth, currDepth)
                s.append((node.left, currDepth+1))
                s.append((node.right, currDepth+1))
        return depth