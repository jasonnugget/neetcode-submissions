class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        track = set()

        for i in nums:
            if i - 1 not in nums:
                track.add(i)
        
        sol = 0
        for j in track:
            count = 0
            while j in nums:
                count += 1
                j += 1
            sol = max(sol, count)

        return sol