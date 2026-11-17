class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        x1 = 0
        y1 = 0

        for i in range(len(points)):
            x2, y2 = points[i]
            dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
            heapq.heappush(minHeap, (dist, i))

        sol = []
        for i in range(k):
            dist, index = heapq.heappop(minHeap)
            sol.append(points[index])

        return sol
