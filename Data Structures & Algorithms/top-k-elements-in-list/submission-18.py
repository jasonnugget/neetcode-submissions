class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        checker = defaultdict(int)
        res = []

        for j in nums:
            checker[j] += 1

        for i, j in checker.items():
            bucket[j].append(i)

        for i in range(len(bucket) - 1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
