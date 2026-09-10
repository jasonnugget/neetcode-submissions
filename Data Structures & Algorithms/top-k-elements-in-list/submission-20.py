class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        bucket = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] += 1
        
        for i in count:
            bucket[count[i]].append(i)
    
        res = []
        for i in range(len(nums), -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res

        


        