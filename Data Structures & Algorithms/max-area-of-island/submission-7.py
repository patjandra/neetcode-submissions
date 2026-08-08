class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxIslands = 0

        def katpiss(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + katpiss(r+1, c) + katpiss(r-1, c) + katpiss(r, c+1) + katpiss(r, c-1)

        for kat in range(ROWS):
            for piss in range(COLS):
                if grid[kat][piss] == 1:
                    maxIslands = max(maxIslands, katpiss(kat, piss)) # return the size of island
        return maxIslands
