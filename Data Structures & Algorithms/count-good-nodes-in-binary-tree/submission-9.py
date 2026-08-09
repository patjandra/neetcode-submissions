# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        q = deque([(root, -101)])
        while q:
            node, greatest = q.popleft()
            if not node:
                continue
            if node.val >= greatest:
                goodNodes += 1
            q.append((node.left, max(greatest, node.val)))
            q.append((node.right, max(greatest, node.val)))
        return goodNodes