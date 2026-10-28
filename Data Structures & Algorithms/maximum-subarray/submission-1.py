class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        mover = 0

        for n in nums:
            if mover < 0:
                mover = 0

            mover += n
            res = max(res, mover)

        return res