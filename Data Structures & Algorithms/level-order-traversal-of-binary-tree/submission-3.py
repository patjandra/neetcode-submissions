# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        out = []
        while q:
            sublist = []
            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    sublist.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if sublist:
                out.append(sublist)
        return out