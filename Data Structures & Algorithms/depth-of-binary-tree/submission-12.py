# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        s = deque([(root, 1)])
        depth = 0
        while s:
            node, d = s.popleft()
            if node:
                depth = max(depth, d)
                s.append((node.left, depth+1))
                s.append((node.right, depth+1))
        return depth