class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            res = max(res, height * width)

            if heights[l] > heights[r]:
                r -= 1
            
            else:
                l += 1

        return res
