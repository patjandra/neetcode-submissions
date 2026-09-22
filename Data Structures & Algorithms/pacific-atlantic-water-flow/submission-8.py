class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # iterate edges and separately store pacific & atlantic edges
        # dfs/bfs through an oceans edges
            # mark as visited when height >= current height (can flow down to ocean from there)
        # return list of coordinates shared between ocean's visited lists (both oceans are reachable from them)

        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        pacificCells = []
        atlanticCells = []
        for r in range(ROWS):
            pacificCells.append((r, 0))
            atlanticCells.append((r, COLS-1))
        for c in range(COLS):
            pacificCells.append((0, c))
            atlanticCells.append((ROWS-1, c))

        def bfs(lst):
            visited = set()
            for r, c in lst:
                q = deque([(r, c)])
                visited.add((r, c))
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
        print(pacificVisited)
        print(atlanticVisited)
        return [[r, c] for r, c in pacificVisited & atlanticVisited]