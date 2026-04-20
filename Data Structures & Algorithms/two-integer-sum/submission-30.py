class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSet = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in seenSet:
                return [seenSet[diff], i]
            seenSet[j] = i