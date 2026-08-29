class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = 1
                    grid[r][c] = 0
                    q = deque([(r, c)])
                    while q:
                        row, col = q.popleft()
                        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                            newR, newC = row+dr, col+dc
                            if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                                grid[newR][newC] = 0
                                area += 1
                                q.append((newR, newC))
                    maxArea = max(maxArea, area)
        return maxArea