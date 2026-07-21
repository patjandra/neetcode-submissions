# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #   return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        stack = [(root, 1)]
        depth = 0
        while stack and root:
            curr = stack.pop()
            depth = max(depth, curr[1])
            if curr[0].left:
                stack.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                stack.append((curr[0].right, curr[1]+1))
        return depth