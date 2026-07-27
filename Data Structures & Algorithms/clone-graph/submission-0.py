"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        start = node
        oldNew = {}
        s = [start]
        visited = set()
        visited.add(start)

        while s:
            node = s.pop()
            oldNew[node] = Node(node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    s.append(neighbor)

        for old, new in oldNew.items():
            for neighbor in old.neighbors:
                newNeighbor = oldNew[neighbor]
                new.neighbors.append(newNeighbor)
        return oldNew[start]