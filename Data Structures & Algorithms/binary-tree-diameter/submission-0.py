# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # get maxLeft = maxRight for each node
        # maintain largest diamter
        largestD = 0

        def height(root):
            nonlocal largestD

            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            diameter = leftHeight + rightHeight
            largestD = max(largestD, diameter)
            return 1 + max(leftHeight, rightHeight)

        height(root)
        return largestD