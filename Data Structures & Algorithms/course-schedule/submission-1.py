class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct adjacency map
        # maintain array of condition of each node (Unvisited, Visiting, Visited)
        # dfs each course, returns True if no cycle, False if cycle
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        Unvisited = 0
        Visiting = 1
        Visited = 2
        status = [Unvisited] * numCourses

        def dfs(node):
            if status[node] == Visiting:
                return False
            if status[node] == Visited:
                return True
            status[node] = Visiting
            for i in g[node]:
                if not dfs(i):
                    return False
            status[node] = Visited
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True