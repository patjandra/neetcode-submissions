# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        stack = [root]
        mapper = {None: (0,0)} # node : (height, diameter)

        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in mapper:
                stack.append(curr.left)
            elif curr.right and curr.right not in mapper:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                heightL, diameterL = mapper[curr.left]
                heightR, diameterR = mapper[curr.right]
                mapper[curr] = (1+max(heightL, heightR), max(heightL + heightR, diameterL, diameterR))
        return mapper[root][1]