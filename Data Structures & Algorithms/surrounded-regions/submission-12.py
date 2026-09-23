class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        edges = set()
        for r in range(ROWS):
            edges.add((r, 0))
            edges.add((r, COLS-1))
        for c in range(1, COLS-1):
            edges.add((0, c))
            edges.add((ROWS-1, c))

        def dfs(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == 'O':
                board[r][c] = 'T'
                for dr, dc in directions:
                    newR, newC = r+dr, c+dc
                    dfs(newR, newC)
        for r, c in edges:
            dfs(r, c)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'