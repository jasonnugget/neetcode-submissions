class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)
        q = deque()

        count = 0
        while maxHeap or q:
            count += 1

            if maxHeap:
                num = 1 + heapq.heappop(maxHeap)
                if num:
                    q.append([num, count + n])

            if q and q[0][1] == count:
                heapq.heappush(maxHeap, q.popleft()[0])

        return count
