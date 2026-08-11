class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if (row, col) in visited or not (0 <= row < ROWS) or not (0 <= col < COLS):
                    continue
                visited.add((row, col))
                if grid[row][col] == -1:
                    continue
                grid[row][col] = min(grid[row][col], dist)
                q.append([row+1, col])
                q.append([row-1, col])
                q.append([row, col+1])
                q.append([row, col-1])
            dist += 1