class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for i in nums:
            if (i - 1) not in numsSet:
                length = 0
                while (i + length) in numsSet:
                    length += 1
                
                longest = max(length, longest)

        return longest