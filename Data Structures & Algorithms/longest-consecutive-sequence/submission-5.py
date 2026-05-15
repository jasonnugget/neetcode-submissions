class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)

        res = 0
        for i in numsSet:
            if (i - 1) not in numsSet:
                count = 0
                checker = i
                while(checker in numsSet):
                    count += 1
                    checker += 1
                res = max(res, count)

        return res

        