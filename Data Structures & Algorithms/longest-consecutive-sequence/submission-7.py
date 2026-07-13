class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0
        for i in nums:
            count = 0
            if i + 1 not in nums:
                temp = i
                while(temp in nums):
                    count += 1
                    temp = temp - 1
                result = max(count, result)

        return result
                
