class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        length = len(nums)
        seen.update(nums)
        length_seen = len(seen)
        return length != length_seen