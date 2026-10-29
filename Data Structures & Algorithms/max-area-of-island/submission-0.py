class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0
        def dfs(r, c, path):
            if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return

            visited.add((r, c))
            path.add((r, c))

            dfs(r + 1, c, path)
            dfs(r - 1, c, path)
            dfs(r, c + 1, path)
            dfs(r, c - 1, path)


        for r in range(rows):
            for c in range(cols):
                path = set()
                dfs(r, c, path)

                res = max(res, len(path))

        return res