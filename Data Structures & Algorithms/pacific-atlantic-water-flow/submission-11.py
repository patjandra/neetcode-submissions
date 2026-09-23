class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # capture pacific regions and atlantic regions
        # bfs from each pacific and atlantic cell while heights are >=, building visited sets
        # return list of cells found in both sets (visited means can reach ocean from that cell)
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        pacificCells = set()
        atlanticCells = set()
        for r in range(ROWS):
            pacificCells.add((r, 0))
            atlanticCells.add((r, COLS-1))
        for c in range(COLS):
            pacificCells.add((0, c))
            atlanticCells.add((ROWS-1, c))
        
        def bfs(cells):
            q = deque(cells)
            visited = set(cells)
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newR, newC = row+dr, col+dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited and heights[newR][newC] >= heights[row][col]:
                        q.append((newR, newC))
                        visited.add((newR, newC))
            return visited
        
        pacificSet = bfs(pacificCells)
        atlanticSet = bfs(atlanticCells)
        return [[r, c] for r, c in pacificSet & atlanticSet]