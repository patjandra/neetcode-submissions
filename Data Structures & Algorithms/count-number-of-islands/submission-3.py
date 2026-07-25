class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        numIslands = 0

        def bfs(i, j):
            if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != "1":
                return
            grid[i][j] = "0"
            bfs(i + 1, j)
            bfs(i - 1, j)
            bfs(i, j + 1)
            bfs(i, j - 1)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    numIslands += 1
                    bfs(i, j)
        return numIslands