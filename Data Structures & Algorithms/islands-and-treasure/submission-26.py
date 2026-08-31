class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        level = 1
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row+dr, col+dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == INF:
                        grid[newR][newC] = level
                        q.append((newR, newC))
            level += 1