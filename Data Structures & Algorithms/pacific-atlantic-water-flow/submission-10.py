class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        pacificCells = []
        atlanticCells = []
        for r in range(ROWS):
            pacificCells.append((r, 0))
            atlanticCells.append((r, COLS-1))
        for c in range(COLS):
            pacificCells.append((0, c))
            atlanticCells.append((ROWS-1, c))

        def bfs(cells):
            visited = set(cells)
            q = deque(cells)
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row+dr, col+dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited and heights[newR][newC] >= heights[row][col]:
                        q.append((newR, newC))
                        visited.add((newR, newC))
            return visited
        
        pacificVisited = bfs(pacificCells)
        atlanticVisited = bfs(atlanticCells)
        return [[r, c] for r, c in pacificVisited & atlanticVisited]