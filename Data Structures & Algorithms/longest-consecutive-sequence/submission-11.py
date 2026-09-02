class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        track = []
        res = 0
        for j in nums:
            if j - 1 not in nums:
                track.append(j)

        for start in track:
            count = 0
            while start in nums:
                count += 1
                start += 1
            res = max(res, count)

        return res