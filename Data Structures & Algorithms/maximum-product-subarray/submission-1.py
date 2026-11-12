class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxNum, minNum = 1, 1

        for n in nums:
            if n == 0:
                maxNum, minNum = 1, 1
                continue
            
            temp = maxNum * n
            maxNum = max(temp, minNum * n, n)
            minNum = min(temp, minNum * n, n)

            res = max(res, maxNum)

        return res