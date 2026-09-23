class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in edges:
            g[b].append(a)
            g[a].append(b)

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