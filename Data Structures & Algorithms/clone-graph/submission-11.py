"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapper = {}
        visited = set()
        def dfs(node):
            if not node:
                return None
            if node not in visited:
                visited.add(node)
                mapper[node] = Node(node.val)
                for neighbor in node.neighbors:
                    dfs(neighbor)
        dfs(node)
        for old, new in mapper.items():
            for neighbor in old.neighbors:
                newNeighbor = mapper[neighbor]
                new.neighbors.append(newNeighbor)
        return mapper[node] if node else None
