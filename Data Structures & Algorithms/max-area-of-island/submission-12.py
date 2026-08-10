class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c):
            currArea = 0
            q = deque([[r, c,]])
            while q:
                row, col = q.popleft()
                if (0 <= row < ROWS) and (0 <= col < COLS) and grid[row][col] == 1:
                    grid[row][col] = 0
                    currArea += 1
                    q.append([row+1, col])
                    q.append([row-1, col])
                    q.append([row, col+1])
                    q.append([row, col-1])
            return currArea
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        return maxArea
