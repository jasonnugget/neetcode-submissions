class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()

        def validAdd(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or (r, c) in visited:
                return

            q.append([r, c])
            visited.add((r, c))

            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])

        distance = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] < distance:
                    continue
                
                else:
                    grid[r][c] = distance

                validAdd(r + 1, c)
                validAdd(r - 1, c)
                validAdd(r, c + 1)
                validAdd(r, c - 1)

            distance += 1

