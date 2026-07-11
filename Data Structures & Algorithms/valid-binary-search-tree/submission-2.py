# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, -math.inf, math.inf)]) 
        while queue:
            curr = queue.popleft()
            if not (curr[1] < curr[0].val < curr[2]):
                    return False
            if curr[0].left:
                queue.append((curr[0].left, curr[1], curr[0].val))
            if curr[0].right:
                queue.append((curr[0].right, curr[0].val, curr[2]))
        return True