# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # post = left, right, root
        # pre = root, left, right
        # mod pre = root, right, left
        # rev mod pre = left, right, root
        traversal = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                traversal.append(curr.val)
                curr = curr.right
            curr = stack.pop()
            curr = curr.left

        return traversal[::-1]