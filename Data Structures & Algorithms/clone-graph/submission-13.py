"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew = {} # oldNode : newNode
        visited = set() # Node(s)
        def dfs(node):
            if not node:
                return None
            if node not in visited:
                visited.add(node)
                oldNew[node] = Node(node.val)
                for neighbor in node.neighbors:
                    dfs(neighbor)
        dfs(node)
        for old, new in oldNew.items():
            for neighbor in old.neighbors:
                newNeighbor = oldNew[neighbor]
                new.neighbors.append(newNeighbor)
        return oldNew[node] if node else None