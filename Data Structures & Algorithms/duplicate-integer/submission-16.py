class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)

        return len(new) != len(nums)