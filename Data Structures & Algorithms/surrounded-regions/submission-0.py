class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        edges = set()

        for r in range(rows):
            edges.add((r, 0))
            edges.add((r, cols - 1))

        for c in range(cols):
            edges.add((0, c))
            edges.add((rows - 1, c))

        regions = set()
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] == 'X' or (r, c) in regions:
                return
            
            regions.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return

        for r in range(rows):
            for c in range(cols):
                if (r, c) in edges:
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in regions and board[r][c] == 'O':
                    board[r][c] = 'X'
