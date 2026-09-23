class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        
        Unvisited, Visiting, Visited = 0, 1, 2
        status = [Unvisited] * numCourses

        def dfs(course):
            if status[course] == Visited:
                return True
            elif status[course] == Visiting:
                return False
            status[course] = Visiting
            for nei in g[course]:
                if not dfs(nei):
                    return False
            status[course] = Visited
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True