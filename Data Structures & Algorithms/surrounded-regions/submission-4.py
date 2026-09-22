class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # iterate through edges
        # if edge is 'O'
            # dfs from edge, converting each 'O' to 'T'
        # iterate through board, convert 'O' to 'X' and 'T' to 'O'
        ROWS, COLS = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        edges = set()

        for r in range(ROWS):
            edges.add((r, 0))
            edges.add((r, COLS-1))
        for c in range(COLS):
            edges.add((0, c))
            edges.add((ROWS-1, c))

        def dfs(r, c):
            if not(0 <= r < ROWS) or not(0 <= c < COLS) or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                dfs(newR, newC)
        
        for r, c in edges:
            if board[r][c] == 'O':
                dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'