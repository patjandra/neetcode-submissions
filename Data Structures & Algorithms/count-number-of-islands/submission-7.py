class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        numIslands = 0

        def dfs(row, col):
            if row < 0 or row >= r or col < 0 or col >= c or grid[row][col] != "1":
                return
            grid[row][col] = "0"
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for row in range(r):
            for col in range(c):
                if grid[row][col] == "1":
                    numIslands += 1
                    dfs(row, col)
        return numIslands