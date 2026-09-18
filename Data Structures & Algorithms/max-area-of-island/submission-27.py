class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        maxArea = 0

        def dfs(r, c):
            area = 1
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    area += dfs(nr, nc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea