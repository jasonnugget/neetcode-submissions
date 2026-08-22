class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for i,j in enumerate(nums):
            temp = target - j
            if temp in seen:
                return [seen[temp], i]
            else:
                seen[j] = i
                