class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)

        for i, j in enumerate(nums):
            if target - j in check:
                return[check[target - j], i]

            else:
                check[j] = i
            