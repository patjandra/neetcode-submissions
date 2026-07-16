# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        def dfs(node, largest):
            nonlocal goodNodes

            if not node:
                return 0
            if node.val >= largest:
                goodNodes += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, largest)
                dfs(node.right, largest)

        dfs(root, root.val)
        return goodNodes