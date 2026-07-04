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
        stack = [root]
        curr = root

        #1, 3
        while stack and curr:
            for _ in range(len(curr.children)):
                stack.append(curr.children[-1])
                curr.children.remove(curr.children[-1])
            curr = stack[-1]
            if not curr.children:
                traversal.append(curr.val)
                stack.pop()

        return traversal