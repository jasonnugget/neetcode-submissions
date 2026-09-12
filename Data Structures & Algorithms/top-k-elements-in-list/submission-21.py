class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = defaultdict(int)
        bucketSort = [[] for i in range(len(nums) + 1)]
        res = []

        for i in nums:
            tracker[i] += 1

        for i in tracker:
            count = tracker[i]
            bucketSort[count].append(i)

        for i in range(len(nums), 0, -1):
            for j in bucketSort[i]:
                res.append(j)
                if len(res) == k:
                    return res