class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.num = 0

        def dfs(r, c):
            grid[r][c] = "0"
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == "1":
                    dfs(newR, newC)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.num += 1
                    dfs(r, c)
        return self.num