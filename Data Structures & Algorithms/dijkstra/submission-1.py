class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = {i:[] for i in range(n)}

        for s, d, w in edges:
            adjList[s].append([d, w])

        minHeap = [[0, src]]
        shortest = {}
        while minHeap:
            w1, s = heapq.heappop(minHeap)
            if s in shortest:
                continue

            shortest[s] = w1
            for d, w2 in adjList[s]:
                if d in shortest:
                    continue
                heapq.heappush(minHeap, [w1 + w2, d])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest