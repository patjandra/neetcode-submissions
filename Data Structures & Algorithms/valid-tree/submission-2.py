class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in edges:
            g[b].append(a)
            g[a].append(b)
        Unvisited, Visiting, Visited = 0, 1, 2
        status = [Unvisited] * n

        def dfs(node, parent):
            if status[node] == Visiting:
                return False
            elif status[node] == Visited:
                return True
            status[node] = Visiting
            for nei in g[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            status[node] = Visited
            return True
        
        if not dfs(0, -1):
            return False
        return all(state == Visited for state in status)