class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        edges = set()
        for r in range(ROWS):
            edges.add((r, 0))
            edges.add((r, COLS-1))
        for c in range(COLS):
            edges.add((0, c))
            edges.add((ROWS-1, c))

        q = deque(edges)
        while q:
            row, col = q.popleft()
            if board[row][col] == 'O':
                board[row][col] = 'T'
                for dr, dc in directions:
                    newR, newC = row+dr, col+dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and board[newR][newC] == 'O':
                        q.append((newR, newC))
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'