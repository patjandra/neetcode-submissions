class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    newRow, newCol = row+dr, col+dc
                    if 0 <= newRow < ROWS and 0 <= newCol < COLS and grid[newRow][newCol] == INF:
                        grid[newRow][newCol] = grid[row][col] + 1
                        q.append((newRow, newCol))