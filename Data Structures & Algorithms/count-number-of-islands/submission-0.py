class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0

        def dfs(row, col):
            if (row >= len(grid) or row < 0
            or col >= len(grid[0]) or col < 0
            or ((row, col)) in seen
            or grid[row][col] == "0"):
                return False

            seen.add((row, col))
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)

            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j):
                    res += 1


        return res

