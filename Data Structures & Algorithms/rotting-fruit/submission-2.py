class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1

                elif grid[r][c] == 2:
                    rotten.append([r, c])

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]

        minutes = 0
        while rotten and fresh > 0:
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    tempR, tempC = r + dr, c + dc
                    if tempR < 0 or tempR >= rows or tempC < 0 or tempC >= cols or grid[tempR][tempC] != 1:
                        continue

                    rotten.append([tempR, tempC])
                    grid[tempR][tempC] = 2
                    fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1

