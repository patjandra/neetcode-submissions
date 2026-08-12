class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    currArea = 1
                    q.append([r, c])
                    grid[r][c] = 0

                    while q:
                        row, col = q.popleft()
                        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                            newR, newC = row+dr, col+dc
                            if (0 <= newR < ROWS) and (0 <= newC < COLS) and grid[newR][newC] == 1:
                                currArea += 1
                                q.append([newR, newC])
                                grid[newR][newC] = 0
                    maxArea = max(maxArea, currArea)
        return maxArea