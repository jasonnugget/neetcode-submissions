class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for numbers in nums:
            count[numbers] += 1
        
        for n, c in count.items():
            freq[c].append(n)

        res = []
        
        for i in range(len(nums), 0, -1):
            if freq[i]:
                for j in freq[i]:
                    res.append(j)
                    if len(res) == k:
                        return res
