class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,j in enumerate(nums):
            k = target - j
            if k in seen:
                return [seen[k], i]
            seen[j] = i

            