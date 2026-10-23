class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-x for x in nums]
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        temp = []
        tempNum = 0
        for i in range(self.k):
            tempNum = -heapq.heappop(self.nums)
            temp.append(tempNum)

        for i in temp:
            heapq.heappush(self.nums, -i)

        return tempNum
        
