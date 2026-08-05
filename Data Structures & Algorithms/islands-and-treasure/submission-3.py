class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(row, col):
            q = deque([(row,col)])
            visited = set()
            dist = 0
            while q:
                for _ in range(len(q)):
                    ro, co = q.popleft()
                    if (ro, co) in visited or ro < 0 or ro >= r or co < 0 or co >= c:
                        continue
                    visited.add((ro, co))
                    if grid[ro][co] == -1:
                        continue
                    grid[ro][co] = min(grid[ro][co], dist)
                    q.append((ro+1, co))
                    q.append((ro-1, co))
                    q.append((ro, co+1))
                    q.append((ro, co-1))
                dist += 1

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    bfs(i, j)