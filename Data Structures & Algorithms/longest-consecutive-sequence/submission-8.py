class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0
        for i in numsSet:
            count = 0
            if i + 1 not in numsSet:
                temp = i
                while(temp in numsSet):
                    count += 1
                    temp = temp - 1
                result = max(count, result)

        return result
                
