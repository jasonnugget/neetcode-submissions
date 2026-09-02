class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        check = defaultdict(int)
        res = []

        for i in nums:
            check[i] += 1

        for i, j in check.items():
            bucket[j].append(i)

        for i in range(len(nums), 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
