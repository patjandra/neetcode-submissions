class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            grid[r][c] = 0
            area = 1
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                newR, newC = r+dr, c+dc
                if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                    area += dfs(newR, newC)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))
        return maxArea