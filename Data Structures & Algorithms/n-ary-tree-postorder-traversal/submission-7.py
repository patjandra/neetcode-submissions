"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        traversal = []

        def dfs(node):
            if not node:
                return
            for i in range(len(node.children)):
                dfs(node.children[i])
            traversal.append(node.val)
        dfs(root)
        return traversal