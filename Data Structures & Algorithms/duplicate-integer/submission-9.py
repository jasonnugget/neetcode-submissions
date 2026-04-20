class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_hash = {}

        for i, j in enumerate(nums):
            new_hash[j] = i
        length = len(nums)
        length2 = len(new_hash)
        if length == length2:
            return False
        else:
            return True
        