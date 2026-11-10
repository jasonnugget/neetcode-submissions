class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        trav = 0

        for n in nums:
            trav += n
            trav = max(trav, n)
            res = max(res, trav)

        return res