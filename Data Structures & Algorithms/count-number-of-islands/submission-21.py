class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num = 0
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    num += 1
                    q = deque([[r, c]])
                    while q:
                        row, col = q.popleft()
                        grid[row][col] = "0"
                        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                            newR, newC = row+dr, col+dc
                            if (newR, newC) in visited or not (0 <= newR < ROWS) or not (0 <= newC < COLS) or grid[newR][newC] != "1":
                                continue
                            q.append([newR, newC])
                            visited.add((newR, newC))
        return num