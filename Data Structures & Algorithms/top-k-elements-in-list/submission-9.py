class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        outputlist = []

        for i, j in enumerate(nums):
            seen[j] += 1
        
        result = dict(sorted(seen.items(), key=lambda x: x[1], reverse = True))

        dictKeys = list(result.keys())

        for a in range(k):
            outputlist.append(dictKeys[a])

        return outputlist