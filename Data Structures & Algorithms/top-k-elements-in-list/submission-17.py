class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for j in nums:
            count[j] += 1

        for key, val in count.items():
            freq[val].append(key)

        sol = []

        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                sol.append(j)
                if len(sol) == k:
                    return sol
