class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited:
                    continue

                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1

        return res