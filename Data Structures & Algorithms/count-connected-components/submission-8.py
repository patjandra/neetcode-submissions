from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        comps = 0

        for i in range(n):
            if i in visited:
                continue

            comps += 1
            q = deque([i])
            visited.add(i)

            while q:
                node = q.popleft()

                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        return comps