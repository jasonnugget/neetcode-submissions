class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i:[] for i in range(1, n + 1)}

        for s, t, w in times:
            adjList[s].append([t, w])

        minHeap = [[0, k]]
        time = 0
        shortest = {}
        while minHeap:
            w1, s = heapq.heappop(minHeap)
            if s in shortest:
                continue

            shortest[s] = w1
            time = w1
            for target, weight in adjList[s]:
                if target in shortest:
                    continue
                heapq.heappush(minHeap, [w1 + weight, target])

        for i in range(1, n + 1):
            if i not in shortest:
                return -1

        return time