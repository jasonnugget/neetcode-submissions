class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                
                if grid[r][c] == 1:
                    fresh += 1

        time = 0
        while q and fresh > 0:
            time += 1
            for i in range(len(q)):
                r, c = q.popleft()

                for tr, tc in directions:
                    if r + tr < 0 or r + tr >= rows or c + tc < 0 or c + tc >= cols or grid[r + tr][c + tc] != 1:
                        continue

                    fresh -= 1
                    grid[r + tr][c + tc] = 2
                    q.append([r + tr, c + tc])

        return time if fresh <= 0 else -1


