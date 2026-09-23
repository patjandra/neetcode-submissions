class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # convert prereqs to adj list
        # create status list
        # dfs through courses

        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        unvisited, visiting, visited = 0, 1, 2
        status = [unvisited] * numCourses
    
        def dfs(node):
            if status[node] == visited:
                return True
            if status[node] == visiting:
                return False
            status[node] = visiting
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            status[node] = visited
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True