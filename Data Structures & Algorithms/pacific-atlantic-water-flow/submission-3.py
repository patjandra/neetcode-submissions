class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = deque(), deque()
        pSeen, aSeen = set(), set()

        for i in range(COLS):
            pacific.append([0, i])
            pSeen.add((0, i))
        
        for i in range(1, ROWS):
            pacific.append([i, 0])
            pSeen.add((i, 0))
        
        for i in range(COLS):
            atlantic.append([ROWS-1, i])
            aSeen.add((ROWS-1, i))

        for i in range(ROWS-1):
            atlantic.append([i, COLS-1])
            aSeen.add((i, COLS-1))
        
        def getCoords(q, seen):
            while q:
                i, j = q.popleft()
                for rOff, cOff in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    r, c = i + rOff, j + cOff
                    if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in seen and heights[i][j] <= heights[r][c]:
                        seen.add((r, c))
                        q.append([r, c])

        getCoords(pacific, pSeen)
        getCoords(atlantic, aSeen)
        return list(pSeen.intersection(aSeen))