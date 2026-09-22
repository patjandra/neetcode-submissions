"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew = {}
        visited = set()
        def dfs(node):
            if not node:
                return None
            if node not in visited:
                oldNew[node] = Node(node.val)
                visited.add(node)
                for n in node.neighbors:
                    dfs(n)
        dfs(node)
        for old, new in oldNew.items():
            for n in old.neighbors:
                newN = oldNew[n]
                new.neighbors.append(newN)
        return oldNew[node] if node else None