class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dist = 0

        def add(row, col):
            if (row, col) in visited or row < 0 or col < 0 or row >= r or col >= c or grid[row][col] == -1:
                return
            visited.add((row, col))
            q.append((row, col))

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i, j))
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = dist
                add(x+1, y)
                add(x-1, y)
                add(x, y+1)
                add(x, y-1)
            dist += 1             