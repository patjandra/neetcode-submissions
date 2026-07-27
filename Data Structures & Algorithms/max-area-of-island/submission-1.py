class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        maxArea = 0

        def dfs(row, col):
            if row < 0 or row >= r or col < 0 or col >= c or grid[row][col] != 1:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        for row in range(r):
            for col in range(c):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea