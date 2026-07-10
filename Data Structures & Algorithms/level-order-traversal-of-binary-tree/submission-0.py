# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root, return empty list
        # init queue with root
        # pop from queue till empty
        # add each popped to intermediate list
        # add each popped if left and if right children to queue
        # after all added, add intermediate list to output list
        if not root:
            return []

        out = []
        queue = deque([root])
        while queue:
            level = []
            levelLen = len(queue)
            for _ in range(levelLen):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            out.append(level)
        return out
        
        

