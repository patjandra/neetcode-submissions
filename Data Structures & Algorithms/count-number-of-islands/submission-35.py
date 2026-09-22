class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        numIslands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    numIslands += 1
                    q = deque([(r, c)])
                    grid[r][c] = "0"
                    while q:
                        row, col = q.popleft()
                        for dr, dc in directions:
                            newR, newC = row+dr, col+dc
                            if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == "1":
                                q.append((newR, newC))
                                grid[newR][newC] = "0"
        return numIslands