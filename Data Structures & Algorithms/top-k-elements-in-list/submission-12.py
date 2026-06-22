class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []

        for i in nums:
            count[i] += 1
        
        for j in range(k):
            maxNum = 0
            storeKey = 0
            for key, val in count.items():
                temp = maxNum
                maxNum = max(maxNum, val)
                if temp != maxNum:
                    storeKey = key
            res.append(storeKey)
            count[storeKey] = 0

        return res
                

            