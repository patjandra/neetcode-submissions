"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        mapper = {}

        def dfs(node):
            if not node:
                return None
            if node not in visited:
                visited.add(node)
                mapper[node] = Node(node.val)
                for n in node.neighbors:
                    dfs(n)
        dfs(node)
        for old, new in mapper.items():
            for n in old.neighbors:
                newN = mapper[n]
                new.neighbors.append(newN)
        return mapper[node] if node else None