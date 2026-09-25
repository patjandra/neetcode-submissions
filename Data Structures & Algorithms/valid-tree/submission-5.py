class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree has no cycle and is connected
        # since we just have a list of undirected edges, need to create adj list (node:children)
        # use visited set to bfs through
            # if we find a node in visited that is not the parent, we have a cycle
            # if we find at the end that len(vistited) != n, we have disjoint sets
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n