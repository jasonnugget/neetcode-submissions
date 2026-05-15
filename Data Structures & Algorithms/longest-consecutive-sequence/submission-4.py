class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        for i in nums:
            if (i - 1) not in nums:
                count = 0
                checker = i
                while(checker in nums):
                    count += 1
                    checker += 1
                res = max(res, count)

        return res

        