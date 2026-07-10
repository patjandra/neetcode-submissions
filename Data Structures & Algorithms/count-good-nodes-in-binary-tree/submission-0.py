# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSeen):
            if not node:
                return 0
            if node.val >= maxSeen:
                maxSeen = node.val
                return 1 + dfs(node.left, maxSeen) + dfs(node.right, maxSeen)
            else:
                return dfs(node.left, maxSeen) + dfs(node.right, maxSeen)

        return dfs(root, root.val)