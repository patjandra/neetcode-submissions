# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return [0, True]
            left = height(node.left)
            right = height(node.right)
            isBalanced = False
            if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
                isBalanced = True
            return [1 + max(left[0], right[0]), isBalanced]
        return height(root)[1]