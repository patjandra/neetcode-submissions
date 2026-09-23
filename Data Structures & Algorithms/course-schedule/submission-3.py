class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        
        Unvisited, Visiting, Visited = 0, 1, 2
        status = [Unvisited] * numCourses

        def dfs(node):
            if status[node] == Visited:
                return True
            if status[node] == Visiting:
                return False
            status[node] = Visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            status[node] = Visited
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True