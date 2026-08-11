"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        visited = set()
        def dfs(node):
            if not node:
                return None
            if node not in visited:
                visited.add(node)
                hashmap[node] = Node(node.val)
                for neighbor in node.neighbors:
                    dfs(neighbor)
        dfs(node)
        for old, new in hashmap.items():
            for neighbor in old.neighbors:
                newNeighbor = hashmap[neighbor]
                new.neighbors.append(newNeighbor)
        return hashmap[node] if node else None            