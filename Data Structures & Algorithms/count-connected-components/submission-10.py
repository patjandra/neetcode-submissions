class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeEdges = defaultdict(list)
        for a, b in edges:
            nodeEdges[a].append(b)
            nodeEdges[b].append(a)
        
        visited = set()
        def dfs(node, edges):
            if node in visited:
                return

            visited.add(node)

            for nei in nodeEdges[node]:
                dfs(nei, nodeEdges[nei])

        comps = 0
        for i in range(n):
            if i not in visited:
                dfs(i, nodeEdges[i])
                comps += 1
        return comps