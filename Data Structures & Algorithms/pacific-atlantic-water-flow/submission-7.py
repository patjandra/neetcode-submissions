class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:



        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        pacificPoints = []
        atlanticPoints = []
        for i in range(ROWS):
            pacificPoints.append([i, 0]) # pacific vert
            atlanticPoints.append([i, COLS-1]) # atlantic vert
        for i in range(COLS):
            pacificPoints.append([0, i]) # pacific horiz
            atlanticPoints.append([ROWS-1, i]) # atlantic horiz

        def bfs(lst, visited): 
            for r, c in lst:
                if (r, c) in visited:
                    continue
                q = deque([(r, c)])
                visited.add((r, c))
                while q:
                    row, col = q.popleft()
                    for dr, dc in directions:
                        newR, newC = row+dr, col+dc
                        if 0 <= newR < ROWS and 0 <= newC < COLS and (newR, newC) not in visited and heights[newR][newC] >= heights[row][col]:
                            q.append((newR, newC))
                            visited.add((newR, newC))
        pacific = set()
        atlantic = set()
        bfs(pacificPoints, pacific)
        bfs(atlanticPoints, atlantic)
        return [[r, c] for r, c in pacific & atlantic]