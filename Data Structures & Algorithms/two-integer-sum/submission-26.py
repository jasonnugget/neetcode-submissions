class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevCheck = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevCheck:
                return [prevCheck[diff], i]
            prevCheck[n] = i
        