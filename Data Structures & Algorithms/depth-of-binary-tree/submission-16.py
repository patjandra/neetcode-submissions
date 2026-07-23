# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = [[root, 1]]
        maxD = 0
        while s:
            node, dep = s.pop()
            if node:
                maxD = max(maxD, dep)
                s.append([node.left, dep+1])
                s.append([node.right, dep+1])
        return maxD