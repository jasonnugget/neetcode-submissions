class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        solMax = 0
        for i in range(len(nums)):
            count = 0
            if nums[i] + 1 in numSet:
                continue
            num = nums[i]
            while(num in numSet):
                count += 1
                num -= 1
            solMax = max(solMax, count)

        return solMax

