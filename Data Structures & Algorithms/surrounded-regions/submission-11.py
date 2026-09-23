class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        for r in range(ROWS):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][COLS-1] == 'O':
                q.append((r, COLS-1))
        for c in range(1, COLS-1):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[ROWS-1][c] == 'O':
                q.append((ROWS-1, c))

        while q:
            row, col = q.popleft()
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