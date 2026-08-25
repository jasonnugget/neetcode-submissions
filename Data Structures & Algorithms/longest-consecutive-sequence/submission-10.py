class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        check = []
        sol = 0

        for i in nums:
            if i - 1 not in nums:
                check.append(i)

        for i in check:
            count = 0
            while i in nums:
                count += 1
                i += 1
            sol = max(count, sol)

        return sol
