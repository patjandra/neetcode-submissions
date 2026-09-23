class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # don't have any methods to traverse graph
        # construct an adjacency list (map nodes to children)
        # dfs through adjacency matrix with visited set to identify any cycles
        # compare visited set to number of nodes to ensure connectivity from dfs
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in g[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visited) == n