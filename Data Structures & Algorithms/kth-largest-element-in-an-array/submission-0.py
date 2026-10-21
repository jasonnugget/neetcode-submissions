import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []

        for n in nums:
            if len(res) == k:
                if res[0] < n:
                    heapq.heappop(res)
                    heapq.heappush(res, n)

                else:
                    continue

            else:
                heapq.heappush(res, n)


        return heapq.heappop(res)