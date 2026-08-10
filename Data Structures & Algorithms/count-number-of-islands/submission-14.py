class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0

        def bfs(r, c):
            q = deque([[r, c]])
            while q:
                row, col = q.popleft()
                if (0 <= row < ROWS) and (0 <= col < COLS) and grid[row][col] == "1":
                    grid[row][col] = "0"
                    q.append([row+1, col])
                    q.append([row-1, col])
                    q.append([row, col+1])
                    q.append([row, col-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    numIslands += 1
                    bfs(r, c,)
        return numIslands