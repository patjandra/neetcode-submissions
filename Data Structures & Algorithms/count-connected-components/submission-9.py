class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # have a visited set
        # create a mapping of node to edge
        # dfs each n, adding each node to visited set
        # increment count of components
        # return count

        nodeEdges = defaultdict(list)
        for a, b in edges:
            nodeEdges[a].append(b)
            nodeEdges[b].append(a)
        
        visited = set()
        def dfs(node, edges):
            if node in visited:
                return
            visited.add(node)
            for n in nodeEdges[node]:
                dfs(n, nodeEdges[n])

        comps = 0
        for i in range(n):
            if i not in visited:
                dfs(i, nodeEdges[i])
                comps += 1
        return comps