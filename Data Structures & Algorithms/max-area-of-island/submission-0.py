class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        area = 0

        def dfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    area = max(area, dfs(i, j))
        return area
