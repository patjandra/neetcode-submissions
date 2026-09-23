class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        def canFinish():
            g = defaultdict(list)
            for a, b in prerequisites:
                g[a].append(b)
            Unvisited, Visiting, Visited = 0, 1, 2
            status = [Unvisited] * numCourses
            def dfs(node):
                if status[node] == Visited:
                    return True
                elif status[node] == Visiting:
                    return False
                status[node] = Visiting
                for nei in g[node]:
                    if not dfs(nei):
                        return False
                status[node] = Visited
                order.append(node)
                return True
            for i in range(numCourses):
                if not dfs(i):
                    return False
            return True
        
        if canFinish():
            return order
        return []