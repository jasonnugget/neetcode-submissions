class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, j in enumerate(nums):
            val = target - j
            if val in seen:
                return[seen[val], i]
            seen[j] = i