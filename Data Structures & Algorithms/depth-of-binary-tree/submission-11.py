# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = [[root, 0]]
        depth = 0
        while s:
            node, dep = s.pop()
            if node:
                depth = max(depth, dep+1)
                s.append([node.left, dep+1])
                s.append([node.right, dep+1])
        return depth