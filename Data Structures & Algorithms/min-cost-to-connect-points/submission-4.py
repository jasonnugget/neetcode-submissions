class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adjList = {i:[] for i in range(N)}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))

        visited = set()
        minHeap = [[0, 0]]
        res = 0

        while len(visited) != N:
            distance, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            
            visited.add(i)
            res += distance
            for dist, to in adjList[i]:
                if to not in visited:
                    heapq.heappush(minHeap, (dist, to))

        return res