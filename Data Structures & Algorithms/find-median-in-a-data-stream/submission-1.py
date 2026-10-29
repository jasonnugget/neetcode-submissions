class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)

        # if values too big are in the small one:
        if self.small and self.large and self.small[0] > self.large[0]:
            temp = heapq.heappop_max(self.small)
            heapq.heappush(self.large, temp)

        # if they are uneven
        if len(self.small) > len(self.large) + 1:
            temp = heapq.heappop_max(self.small)
            heapq.heappush(self.large, temp)
        if len(self.large) > len(self.small) + 1:
            temp = heapq.heappop(self.large)
            heapq.heappush_max(self.small, temp)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (self.large[0] + self.small[0]) / 2
        