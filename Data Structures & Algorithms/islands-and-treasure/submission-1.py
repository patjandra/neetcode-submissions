class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])

        def bfs(row, col):
            visited = set() # visited (row,col)
            level = 0
            q = deque([(row,col)])

            while q:
                for _ in range(len(q)):
                    pair = q.popleft()
                    if pair in visited or pair[0] < 0 or pair[0] >= r or pair[1] < 0 or pair[1] >= c:
                        continue
                    if grid[pair[0]][pair[1]] == -1:
                        visited.add(pair)
                        continue
                    if grid[pair[0]][pair[1]] != 0:
                        if grid[pair[0]][pair[1]] == 2147483647:
                            grid[pair[0]][pair[1]] = level
                        else:
                            grid[pair[0]][pair[1]] = min(grid[pair[0]][pair[1]], level)
                    visited.add(pair)
                    q.append((pair[0]+1, pair[1]))
                    q.append((pair[0]-1, pair[1]))
                    q.append((pair[0], pair[1]+1))
                    q.append((pair[0], pair[1]-1))
                level += 1

        for row in range(r):
            for col in range(c):
                if grid[row][col] == 0: 
                    bfs(row, col)