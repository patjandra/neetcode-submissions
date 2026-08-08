class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        variableIG = 0

        def katpiss(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            katpiss(r+1, c)
            katpiss(r-1, c)
            katpiss(r, c+1)
            katpiss(r, c-1)

        for kat in range(ROWS):
            for piss in range(COLS):
                if grid[kat][piss] == "1":
                    variableIG += 1
                    katpiss(kat, piss)
        return variableIG
