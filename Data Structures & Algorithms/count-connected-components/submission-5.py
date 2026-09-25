class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list of node to nei from edges
        # iterate over n
        # if n not in visited, dfs
        # return number of dfs calls

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        comps = 0
        for i in range(n):
            if i not in visited:
                comps += 1
                dfs(i)
        return comps