"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new = {}
        visited = set()

        def dfs(node):
            if not node:
                return None
            if node not in visited:
                old_new[node] = Node(node.val)
                visited.add(node)
                for n in node.neighbors:
                    dfs(n)
        dfs(node)

        for old, new in old_new.items():
            for n in old.neighbors:
                new_n = old_new[n]
                new.neighbors.append(new_n)
        return old_new[node] if node else None