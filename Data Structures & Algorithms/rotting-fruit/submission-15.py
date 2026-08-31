class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        numFresh = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    numFresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        time = 0
        while q and numFresh:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row+dr, col+dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        numFresh -= 1
                        q.append((newR, newC))
            time += 1
        return time if numFresh == 0 else -1