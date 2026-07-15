class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        if len(prices) == 1:
            return 0

        l = 0
        r = 1

        while r < len(prices):
            res = max(res, prices[r] - prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        
        return res