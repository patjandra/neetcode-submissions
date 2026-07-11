# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numGood = 0
        queue = deque([(root, root.val)])
        while queue:
            curr = queue.popleft()
            node = curr[0]
            largest = curr[1]
            maxSeen = largest
            if node.val >= largest:
                maxSeen = node.val
                numGood += 1
            if node.left:
                queue.append((node.left, maxSeen))
            if node.right:
                queue.append((node.right, maxSeen))
        return numGood