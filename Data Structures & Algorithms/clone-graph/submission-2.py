"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        start = node
        oldNew = {}
        visited = set()
        visited.add(start)

        def dfs(node):
            if not node:
                return None
            oldNew[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        dfs(start)
        for old, new in oldNew.items():
            for neighbor in old.neighbors:
                newNeighbor = oldNew[neighbor]
                new.neighbors.append(newNeighbor)
        return oldNew[start] if node else None