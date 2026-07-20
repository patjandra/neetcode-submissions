# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([root, root.val])
        good = 1
        while q:
            node = q.popleft()
            largestSeen = q.popleft()
            if node.left:
                if node.left.val >= largestSeen:
                    good += 1
                    q.extend([node.left, node.left.val])
                else:
                    q.extend([node.left, largestSeen])
            if node.right:
                if node.right.val >= largestSeen:
                    good += 1
                    q.extend([node.right, node.right.val])
                else:
                    q.extend([node.right, largestSeen])
        return good 