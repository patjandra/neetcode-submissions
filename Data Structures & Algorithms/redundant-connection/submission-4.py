class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # construct adj list excluding one edge at a time
        # run dfs with visited set, if non-cyclical, store excluded edge in output
        # return final output
        out = []
        for i in range(len(edges)):
            copy = edges.copy()
            removed = copy.pop(i)
            adj = defaultdict(list)
            for a, b in copy:
                adj[a].append(b)
                adj[b].append(a)
            
            visited = set()
            def dfs(node, parent):
                if node not in visited:
                    visited.add(node)
                    for nei in adj[node]:
                        if nei == parent:
                            continue
                        if nei in visited:
                            return False
                        if not dfs(nei, node):
                            return False
                return True
            if dfs(list(adj.keys())[0], -1) and len(visited) == len(edges):
                out = removed
        return out
        