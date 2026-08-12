class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num += 1
                    grid[r][c] = "0"
                    q.append([r, c])
                    while q:
                        row, col = q.popleft()
                        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            if (0 <= row+dr < ROWS) and (0 <= col+dc < COLS) and grid[row+dr][col+dc] == "1":
                                q.append([row+dr, col+dc])
                                grid[row+dr][col+dc] = "0"
        return num 