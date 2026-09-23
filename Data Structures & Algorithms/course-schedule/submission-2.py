class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        Unvisited, Visiting, Visited = 0, 1, 2
        status = [Unvisited] * numCourses

        def dfs(node):
            if status[node] == Visiting:
                return False
            if status[node] == Visited:
                return True
            status[node] = Visiting
            for nei in g[node]:
                if not dfs(nei):
                    return False
            status[node] = Visited
            return True

        for i in range(numCourses):
            if status[i] == Unvisited and not dfs(i):
                return False
        return True