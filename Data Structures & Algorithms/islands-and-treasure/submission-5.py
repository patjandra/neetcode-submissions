class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        dist = 0

        def add(r, c):
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1:
                return
            visited.add((r, c))
            q.append((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i, j))
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                add(r+1, c)
                add(r-1, c)
                add(r, c+1)
                add(r, c-1)
            dist += 1             