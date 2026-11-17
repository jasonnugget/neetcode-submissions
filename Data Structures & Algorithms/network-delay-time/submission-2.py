class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1, n + 1)}
        for u, v, t in times:
            adjList[u].append((v, t))
        
        visited = set()
        res = 0
        minHeap = [(0, k)]

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue

            visited.add(n1)
            res = w1

            for n2, w2 in adjList[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(minHeap, (w2 + w1, n2))

        return res if len(visited) == n else -1 
