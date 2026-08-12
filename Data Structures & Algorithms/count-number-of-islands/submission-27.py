class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num = 0
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num += 1
                    q.append([r, c])
                    while q:
                        row, col = q.popleft()
                        grid[row][col] = "0"
                        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            if (row+dr, col+dc) not in visited and (0 <= row+dr < ROWS) and (0 <= col+dc < COLS) and grid[row+dr][col+dc] == "1":
                                q.append([row+dr, col+dc])
                                visited.add((row+dr, col+dc))
        return num 